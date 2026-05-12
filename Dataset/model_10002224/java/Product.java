





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String photoPath;
    private String description;
    private String name;
    private int price;
    private int id;





    private Store store;


    public Product(
        String photoPath,        String description,        String name,        int price,        int id    ) {
        this.photoPath = photoPath;
        this.description = description;
        this.name = name;
        this.price = price;
        this.id = id;
    }


    public String getPhotopath() {
        return photoPath;
    }

    public void setPhotopath(String photoPath) {
        this.photoPath = photoPath;
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
    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }

}