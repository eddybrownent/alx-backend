import express from 'express';
import { promisify } from 'util';
import redis from 'redis';

const listProducts = [
  { itemId: 1, itemName: 'Suitcase 250', price: 50, initialAvailableQuantity: 4 },
  { itemId: 2, itemName: 'Suitcase 450', price: 100, initialAvailableQuantity: 10 },
  { itemId: 3, itemName: 'Suitcase 650', price: 350, initialAvailableQuantity: 2 },
  { itemId: 4, itemName: 'Suitcase 1050', price: 550, initialAvailableQuantity: 5 }
];

function getItemById(itemId) {
  return listProducts.find(product => product.itemId === itemId);
}

const app = express();
const client = redis.createClient();

const reserveStockById = async (itemId, initialAvailableQuantity) => {
  const setAsync = promisify(client.set).bind(client);
  await setAsync(`item.${itemId}`, initialAvailableQuantity);
};

const getCurrentReservedStockById = async (itemId) => {
  const getAsync = promisify(client.get).bind(client);
  const reservedStock = await getAsync(`item.${itemId}`);
  return reservedStock ? parseInt(reservedStock) : 0;
};

// Routes

app.get('/list_products', (req, res) => {
  res.json(listProducts);
});

app.get('/list_products/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  res.json({ ...product, currentQuantity: currentStock });
});

app.get('/reserve_product/:itemId', async (req, res) => {
  const itemId = parseInt(req.params.itemId);
  const product = getItemById(itemId);
  if (!product) {
    res.status(404).json({ status: 'Product not found' });
    return;
  }
  const currentStock = await getCurrentReservedStockById(itemId);
  if (currentStock >= product.initialAvailableQuantity) {
    res.json({ status: 'Not enough stock available', itemId });
    return;
  }
  await reserveStockById(itemId, currentStock + 1);
  res.json({ status: 'Reservation confirmed', itemId });
});

app.listen(1245, () => {
  console.log('Server is running on port 1245');
});
