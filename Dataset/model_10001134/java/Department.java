





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String description;
    private String name;





    private employee employee;


    public Department(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public employee getEmployee() {
        return employee;
    }

    public void setEmployee(employee employee) {
        this.employee = employee;
    }

}