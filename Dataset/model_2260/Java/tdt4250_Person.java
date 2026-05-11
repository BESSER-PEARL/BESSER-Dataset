





import java.util.List;
import java.util.ArrayList;

public class tdt4250_Person  {

    private int ID;
    private String name;



    public tdt4250_Person(
        int ID,        String name    ) {
        this.ID = ID;
        this.name = name;
    }


    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}