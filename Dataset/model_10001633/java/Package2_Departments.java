





import java.util.List;
import java.util.ArrayList;

public class Package2_Departments  {

    private int id;
    private String depname;



    public Package2_Departments(
        int id,        String depname    ) {
        this.id = id;
        this.depname = depname;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getDepname() {
        return depname;
    }

    public void setDepname(String depname) {
        this.depname = depname;
    }


}