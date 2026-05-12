





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String description;
    private String name;
    private int id;



    public Product(
        String description,        String name,        int id    ) {
        this.description = description;
        this.name = name;
        this.id = id;
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
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}