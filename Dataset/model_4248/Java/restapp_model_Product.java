





import java.util.List;
import java.util.ArrayList;

public class restapp_model_Product  {

    private int stock;
    private String name;
    private int status;
    private int id;
    private String description;



    public restapp_model_Product(
        int stock,        String name,        int status,        int id,        String description    ) {
        this.stock = stock;
        this.name = name;
        this.status = status;
        this.id = id;
        this.description = description;
    }


    public int getStock() {
        return stock;
    }

    public void setStock(int stock) {
        this.stock = stock;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getStatus() {
        return status;
    }

    public void setStatus(int status) {
        this.status = status;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }


}