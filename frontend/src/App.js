// src/App.js
import 'antd/dist/reset.css'; // ✅ SOLO este CSS si usas AntD v5
import { Table, Button, Layout, Typography } from 'antd';
import React, { useEffect, useState } from 'react';

const { Header, Content } = Layout;
const { Title } = Typography;

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/items')
      .then(response => response.json())
      .then(data => setItems(data))
      .catch(err => console.error(err));
  }, []);

  const columns = [
    { title: 'ID', dataIndex: 'id', key: 'id' },
    { title: 'Nombre', dataIndex: 'nombre', key: 'nombre' },
    { title: 'Categoría', dataIndex: 'categoria', key: 'categoria' },
    { title: 'Cantidad', dataIndex: 'cantidad', key: 'cantidad' },
    { title: 'Ubicación', dataIndex: 'ubicacion', key: 'ubicacion' }
  ];

  return (
    <Layout style={{ minHeight: '100vh' }}>
      <Header style={{ color: 'white' }}>
        <Title level={3} style={{ color: 'white', margin: 0 }}>Sistema de Inventario SVV</Title>
      </Header>
      <Content style={{ padding: '24px' }}>
        <Button type="primary" style={{ marginBottom: 16 }}>Agregar Item</Button>
        <Table columns={columns} dataSource={items} rowKey="id" />
      </Content>
    </Layout>
  );
}

export default App;

