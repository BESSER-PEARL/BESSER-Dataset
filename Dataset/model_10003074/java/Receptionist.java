





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String attribute2;
    private int id;



    public Receptionist(
        String attribute2,        int id    ) {
        this.attribute2 = attribute2;
        this.id = id;
    }


    public String getAttribute2() {
        return attribute2;
    }

    public void setAttribute2(String attribute2) {
        this.attribute2 = attribute2;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}