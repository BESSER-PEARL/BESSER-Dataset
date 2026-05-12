





import java.util.List;
import java.util.ArrayList;

public class Hotels  {

    private int id;
    private int location;
    private int name;



    public Hotels(
        int id,        int location,        int name    ) {
        this.id = id;
        this.location = location;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getLocation() {
        return location;
    }

    public void setLocation(int location) {
        this.location = location;
    }
    public int getName() {
        return name;
    }

    public void setName(int name) {
        this.name = name;
    }


}