





import java.util.List;
import java.util.ArrayList;

public class Administrator  {

    private int administratorID;
    private String name;



    public Administrator(
        int administratorID,        String name    ) {
        this.administratorID = administratorID;
        this.name = name;
    }


    public int getAdministratorid() {
        return administratorID;
    }

    public void setAdministratorid(int administratorID) {
        this.administratorID = administratorID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}