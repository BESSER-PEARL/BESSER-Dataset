





import java.util.List;
import java.util.ArrayList;

public class projectDsl_Employee  {

    private String name;
    private int weight;
    private int height;





    private projectDsl_Employees projectdsl_employees;


    public projectDsl_Employee(
        String name,        int weight,        int height    ) {
        this.name = name;
        this.weight = weight;
        this.height = height;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getWeight() {
        return weight;
    }

    public void setWeight(int weight) {
        this.weight = weight;
    }
    public int getHeight() {
        return height;
    }

    public void setHeight(int height) {
        this.height = height;
    }

    public projectDsl_Employees getProjectdsl_employees() {
        return projectdsl_employees;
    }

    public void setProjectdsl_employees(projectDsl_Employees projectdsl_employees) {
        this.projectdsl_employees = projectdsl_employees;
    }

}