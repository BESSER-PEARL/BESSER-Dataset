





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private String description;
    private int id;
    private int price;
    private String photoPath;





    private Store store;


    public Product(
        String name,        String description,        int id,        int price,        String photoPath    ) {
        this.name = name;
        this.description = description;
        this.id = id;
        this.price = price;
        this.photoPath = photoPath;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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