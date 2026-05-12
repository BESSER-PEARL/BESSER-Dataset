





import java.util.List;
import java.util.ArrayList;

public class Appliance  {

    private String Price;
    private String Brand;
    private String Model;
    private int Stock;





    private Store store;




    private Order order;


    public Appliance(
        String Price,        String Brand,        String Model,        int Stock    ) {
        this.Price = Price;
        this.Brand = Brand;
        this.Model = Model;
        this.Stock = Stock;
    }


    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }
    public String getBrand() {
        return Brand;
    }

    public void setBrand(String Brand) {
        this.Brand = Brand;
    }
    public String getModel() {
        return Model;
    }

    public void setModel(String Model) {
        this.Model = Model;
    }
    public int getStock() {
        return Stock;
    }

    public void setStock(int Stock) {
        this.Stock = Stock;
    }

    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }
    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}