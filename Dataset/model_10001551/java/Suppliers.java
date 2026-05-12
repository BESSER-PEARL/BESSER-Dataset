





import java.util.List;
import java.util.ArrayList;

public class Suppliers  {

    private String Name;
    private int id;



    public Suppliers(
        String Name,        int id    ) {
        this.Name = Name;
        this.id = id;
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


}