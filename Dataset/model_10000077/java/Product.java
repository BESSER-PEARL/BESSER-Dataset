





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private int id;
    private int price;
    private String description;
    private String name;
    private String photoPath;





    private Store store;


    public Product(
        int id,        int price,        String description,        String name,        String photoPath    ) {
        this.id = id;
        this.price = price;
        this.description = description;
        this.name = name;
        this.photoPath = photoPath;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPhotopath() {
        return photoPath;
    }

    public void setPhotopath(String photoPath) {
        this.photoPath = photoPath;
    }

    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }

}