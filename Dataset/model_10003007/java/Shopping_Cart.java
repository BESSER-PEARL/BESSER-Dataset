





import java.util.List;
import java.util.ArrayList;

public class Shopping_Cart  {

    private int DateCreated;
    private int CartId;
    private int RecordId;
    private int ProductId;
    private int Quantity;





    private Product product;




    private Customer customer;


    public Shopping_Cart(
        int DateCreated,        int CartId,        int RecordId,        int ProductId,        int Quantity    ) {
        this.DateCreated = DateCreated;
        this.CartId = CartId;
        this.RecordId = RecordId;
        this.ProductId = ProductId;
        this.Quantity = Quantity;
    }


    public int getDatecreated() {
        return DateCreated;
    }

    public void setDatecreated(int DateCreated) {
        this.DateCreated = DateCreated;
    }
    public int getCartid() {
        return CartId;
    }

    public void setCartid(int CartId) {
        this.CartId = CartId;
    }
    public int getRecordid() {
        return RecordId;
    }

    public void setRecordid(int RecordId) {
        this.RecordId = RecordId;
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

    public Product getProduct() {
        return product;
    }

    public void setProduct(Product product) {
        this.product = product;
    }
    public Customer getCustomer() {
        return customer;
    }

    public void setCustomer(Customer customer) {
        this.customer = customer;
    }

}