for producto in inventario:
    valor_producto = producto['stock'] * producto['precio']
    valor_total += valor_producto
    total_productos += producto['stock']
    print(f"{producto['id']:<5} {producto['nombre']:<10} {producto['stock']:<10} ${producto['precio']:<10.2f} ${valor_producto:<10.2f}")
