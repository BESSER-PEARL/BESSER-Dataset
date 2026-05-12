





import java.util.List;
import java.util.ArrayList;

public class Staff  {

    private String Name;
    private int id;
    private String type;



    public Staff(
        String Name,        int id,        String type    ) {
        this.Name = Name;
        this.id = id;
        this.type = type;
    }


    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}