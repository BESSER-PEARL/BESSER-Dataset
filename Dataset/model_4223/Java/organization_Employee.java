





import java.util.List;
import java.util.ArrayList;

public class organization_Employee extends ABase {

    private String name;





    private organization_Department organization_department;


    public organization_Employee(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public organization_Department getOrganization_department() {
        return organization_department;
    }

    public void setOrganization_department(organization_Department organization_department) {
        this.organization_department = organization_department;
    }

}