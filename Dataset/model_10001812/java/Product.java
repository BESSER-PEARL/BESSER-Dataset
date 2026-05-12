





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String attribute5;
    private int productId;
    private String Price;
    private String attribute7;
    private String description;
    private String Name;
    private String SKU;
    private String attribute6;
    private String reviews;





    private OrderDetail orderdetail;




    private Category category;




    private Offer_Interface offer_interface;




    private Item item;




    private Department department;




    private Price price;


    public Product(
        String attribute5,        int productId,        String Price,        String attribute7,        String description,        String Name,        String SKU,        String attribute6,        String reviews    ) {
        this.attribute5 = attribute5;
        this.productId = productId;
        this.Price = Price;
        this.attribute7 = attribute7;
        this.description = description;
        this.Name = Name;
        this.SKU = SKU;
        this.attribute6 = attribute6;
        this.reviews = reviews;
    }


    public String getAttribute5() {
        return attribute5;
    }

    public void setAttribute5(String attribute5) {
        this.attribute5 = attribute5;
    }
    public int getProductid() {
        return productId;
    }

    public void setProductid(int productId) {
        this.productId = productId;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getAttribute7() {
        return attribute7;
    }

    public void setAttribute7(String attribute7) {
        this.attribute7 = attribute7;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getSku() {
        return SKU;
    }

    public void setSku(String SKU) {
        this.SKU = SKU;
    }
    public String getAttribute6() {
        return attribute6;
    }

    public void setAttribute6(String attribute6) {
        this.attribute6 = attribute6;
    }
    public String getReviews() {
        return reviews;
    }

    public void setReviews(String reviews) {
        this.reviews = reviews;
    }

    public OrderDetail getOrderdetail() {
        return orderdetail;
    }

    public void setOrderdetail(OrderDetail orderdetail) {
        this.orderdetail = orderdetail;
    }
    public Category getCategory() {
        return category;
    }

    public void setCategory(Category category) {
        this.category = category;
    }
    public Offer_Interface getOffer_interface() {
        return offer_interface;
    }

    public void setOffer_interface(Offer_Interface offer_interface) {
        this.offer_interface = offer_interface;
    }
    public Item getItem() {
        return item;
    }

    public void setItem(Item item) {
        this.item = item;
    }
    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }
    public Price getPrice() {
        return price;
    }

    public void setPrice(Price price) {
        this.price = price;
    }

}