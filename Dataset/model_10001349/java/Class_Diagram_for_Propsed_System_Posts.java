





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Posts  {

    private int id;
    private int department;
    private String name;



    public Class_Diagram_for_Propsed_System_Posts(
        int id,        int department,        String name    ) {
        this.id = id;
        this.department = department;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getDepartment() {
        return department;
    }

    public void setDepartment(int department) {
        this.department = department;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}