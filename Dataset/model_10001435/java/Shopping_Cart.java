





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private int RecordId;
    private int CartId;
    private int DateCreated;
    private int ProductId;
    private int Quantity;





    private Customer customer;




    private Product product;


    public Shopping_Cart(
        int RecordId,        int CartId,        int DateCreated,        int ProductId,        int Quantity    ) {
        this.RecordId = RecordId;
        this.CartId = CartId;
        this.DateCreated = DateCreated;
        this.ProductId = ProductId;
        this.Quantity = Quantity;
    }


    public int getRecordid() {
        return RecordId;
    }

    public void setRecordid(int RecordId) {
        this.RecordId = RecordId;
    }
    public int getCartid() {
        return CartId;
    }

    public void setCartid(int CartId) {
        this.CartId = CartId;
    }
    public int getDatecreated() {
        return DateCreated;
    }

    public void setDatecreated(int DateCreated) {
        this.DateCreated = DateCreated;
    }
    public int getProductid() {
        return ProductId;
    }

    public void setProductid(int ProductId) {
        this.ProductId = ProductId;
    }
    public int getQuantity() {
        return Quantity;
    }

    public void setQuantity(int Quantity) {
        this.Quantity = Quantity;
    }

    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }

}