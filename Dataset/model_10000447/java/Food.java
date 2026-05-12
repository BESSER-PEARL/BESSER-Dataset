





import java.util.List;
import java.util.ArrayList;

public class Food  {

    private boolean prepared;
    private String name;
    private String food_id;
    private boolean served;
    private float price;





    private Items items;




    private app app;


    public Food(
        boolean prepared,        String name,        String food_id,        boolean served,        float price    ) {
        this.prepared = prepared;
        this.name = name;
        this.food_id = food_id;
        this.served = served;
        this.price = price;
    }


    public boolean getPrepared() {
        return prepared;
    }

    public void setPrepared(boolean prepared) {
        this.prepared = prepared;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getFood_id() {
        return food_id;
    }

    public void setFood_id(String food_id) {
        this.food_id = food_id;
    }
    public boolean getServed() {
        return served;
    }

    public void setServed(boolean served) {
        this.served = served;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public Items getItems() {
        return items;
    }

    public void setItems(Items items) {
        this.items = items;
    }
    public app getApp() {
        return app;
    }

    public void setApp(app app) {
        this.app = app;
    }

}