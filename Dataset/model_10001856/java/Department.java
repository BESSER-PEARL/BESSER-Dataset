





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String modules__;
    private int teachers__;
    private String name;
    private int id;



    public Department(
        String modules__,        int teachers__,        String name,        int id    ) {
        this.modules__ = modules__;
        this.teachers__ = teachers__;
        this.name = name;
        this.id = id;
    }


    public String getModules__() {
        return modules__;
    }

    public void setModules__(String modules__) {
        this.modules__ = modules__;
    }
    public int getTeachers__() {
        return teachers__;
    }

    public void setTeachers__(int teachers__) {
        this.teachers__ = teachers__;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}