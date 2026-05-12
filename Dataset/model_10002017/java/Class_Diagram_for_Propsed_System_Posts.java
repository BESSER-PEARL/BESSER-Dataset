





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Propsed_System_Posts  {

    private int id;
    private int department_id;
    private String name;



    public Class_Diagram_for_Propsed_System_Posts(
        int id,        int department_id,        String name    ) {
        this.id = id;
        this.department_id = department_id;
        this.name = name;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getDepartment_id() {
        return department_id;
    }

    public void setDepartment_id(int department_id) {
        this.department_id = department_id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}