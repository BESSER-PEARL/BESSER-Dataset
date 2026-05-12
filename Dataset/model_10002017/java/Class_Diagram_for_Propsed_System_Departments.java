





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Departments  {

    private String depname;
    private int id;



    public Class_Diagram_for_Propsed_System_Departments(
        String depname,        int id    ) {
        this.depname = depname;
        this.id = id;
    }


    public String getDepname() {
        return depname;
    }

    public void setDepname(String depname) {
        this.depname = depname;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}