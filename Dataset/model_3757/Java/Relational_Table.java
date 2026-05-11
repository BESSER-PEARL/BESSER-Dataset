





import java.util.List;
import java.util.ArrayList;

public class Relational_Table  {

    private String name;
    private String id;



    public Relational_Table(
        String name,        String id    ) {
        this.name = name;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}