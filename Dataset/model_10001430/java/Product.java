





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String productName;
    private int productId;
    private String description;
    private float price;
    private int stock;
    private String imageFileName;





    private List<OrderDetail> orderdetails;


    public Product(
        String productName,        int productId,        String description,        float price,        int stock,        String imageFileName    ) {
        this.productName = productName;
        this.productId = productId;
        this.description = description;
        this.price = price;
        this.stock = stock;
        this.imageFileName = imageFileName;
        this.orderdetails = new ArrayList<>();
    }

    public Product(
        String productName,        int productId,        String description,        float price,        int stock,        String imageFileName        ArrayList<OrderDetail> orderdetails    ) {
        this.productName = productName;
        this.productId = productId;
        this.description = description;
        this.price = price;
        this.stock = stock;
        this.imageFileName = imageFileName;
        this.orderdetails = orderdetails;
    }

    public String getProductname() {
        return productName;
    }

    public void setProductname(String productName) {
        this.productName = productName;
    }
    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }
    public String getImagefilename() {
        return imageFileName;
    }

    public void setImagefilename(String imageFileName) {
        this.imageFileName = imageFileName;
    }

    public List<OrderDetail> getOrderdetails() {
        return orderdetails;
    }

    public void addOrderdetail(Orderdetail orderdetail) {
        this.orderdetails.add(orderdetail);
    }

}