





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String type;
    private String name;
    private int id;



    public Person(
        String type,        String name,        int id    ) {
        this.type = type;
        this.name = name;
        this.id = id;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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