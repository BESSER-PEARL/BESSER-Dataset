





import java.util.List;
import java.util.ArrayList;

public class organization_Company extends ABase {

    private String name;





    private List<organization_Department> organization_departments;


    public organization_Company(
        String name    ) {
        super(
        );
        this.name = name;
        this.organization_departments = new ArrayList<>();
    }

    public organization_Company(
        String name        ArrayList<organization_Department> organization_departments    ) {
        this.name = name;
        this.organization_departments = organization_departments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<organization_Department> getOrganization_departments() {
        return organization_departments;
    }

    public void addOrganization_department(Organization_department organization_department) {
        this.organization_departments.add(organization_department);
    }

}