





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String description;
    private int id;
    private String name;



    public Product(
        String description,        int id,        String name    ) {
        this.description = description;
        this.id = id;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}