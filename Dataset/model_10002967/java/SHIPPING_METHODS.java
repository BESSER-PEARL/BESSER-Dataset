





import java.util.List;
import java.util.ArrayList;

public class SHIPPING_METHODS  {

    private String arrival;
    private String address;
    private int price;
    private String createdAt;
    private String _id;
    private String name;





    private PRODUCT product;




    private SHOPPING_HISTORY shopping_history;


    public SHIPPING_METHODS(
        String arrival,        String address,        int price,        String createdAt,        String _id,        String name    ) {
        this.arrival = arrival;
        this.address = address;
        this.price = price;
        this.createdAt = createdAt;
        this._id = _id;
        this.name = name;
    }


    public String getArrival() {
        return arrival;
    }

    public void setArrival(String arrival) {
        this.arrival = arrival;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public PRODUCT getProduct() {
        return product;
    }

    public void setProduct(PRODUCT product) {
        this.product = product;
    }
    public SHOPPING_HISTORY getShopping_history() {
        return shopping_history;
    }

    public void setShopping_history(SHOPPING_HISTORY shopping_history) {
        this.shopping_history = shopping_history;
    }

}