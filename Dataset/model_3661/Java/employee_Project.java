





import java.util.List;
import java.util.ArrayList;

public class employee_Project  {

    private String description;
    private String name;





    private employee_Directory employee_directory;


    public employee_Project(
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

    public employee_Directory getEmployee_directory() {
        return employee_directory;
    }

    public void setEmployee_directory(employee_Directory employee_directory) {
        this.employee_directory = employee_directory;
    }

}