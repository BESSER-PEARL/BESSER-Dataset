





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String type;
    private int id;
    private String name;



    public Product(
        String type,        int id,        String name    ) {
        this.type = type;
        this.id = id;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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