





import java.util.List;
import java.util.ArrayList;

public class CartItem  {

    private int ProductID;
    private String fileName;
    private String Name;
    private int quantity;
    private String Price;
    private int cartID;
    private String subtotal;





    private List<Product> products;




    private ShoppingCart shoppingcart;


    public CartItem(
        int ProductID,        String fileName,        String Name,        int quantity,        String Price,        int cartID,        String subtotal    ) {
        this.ProductID = ProductID;
        this.fileName = fileName;
        this.Name = Name;
        this.quantity = quantity;
        this.Price = Price;
        this.cartID = cartID;
        this.subtotal = subtotal;
        this.products = new ArrayList<>();
    }

    public CartItem(
        int ProductID,        String fileName,        String Name,        int quantity,        String Price,        int cartID,        String subtotal        ArrayList<Product> products    ) {
        this.ProductID = ProductID;
        this.fileName = fileName;
        this.Name = Name;
        this.quantity = quantity;
        this.Price = Price;
        this.cartID = cartID;
        this.subtotal = subtotal;
        this.products = products;
    }

    public int getProductid() {
        return ProductID;
    }

    public void setProductid(int ProductID) {
        this.ProductID = ProductID;
    }
    public String getFilename() {
        return fileName;
    }

    public void setFilename(String fileName) {
        this.fileName = fileName;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getQuantity() {
        return quantity;
    }

    public void setQuantity(int quantity) {
        this.quantity = quantity;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public int getCartid() {
        return cartID;
    }

    public void setCartid(int cartID) {
        this.cartID = cartID;
    }
    public String getSubtotal() {
        return subtotal;
    }

    public void setSubtotal(String subtotal) {
        this.subtotal = subtotal;
    }

    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}