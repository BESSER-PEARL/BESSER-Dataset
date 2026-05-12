





import java.util.List;
import java.util.ArrayList;

public class staff  {

    private String name;





    private List<department> departments;


    public staff(
        String name    ) {
        this.name = name;
        this.departments = new ArrayList<>();
    }

    public staff(
        String name        ArrayList<department> departments    ) {
        this.name = name;
        this.departments = departments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<department> getDepartments() {
        return departments;
    }

    public void addDepartment(Department department) {
        this.departments.add(department);
    }

}