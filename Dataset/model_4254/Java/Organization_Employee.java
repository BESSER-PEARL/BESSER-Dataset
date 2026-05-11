





import java.util.List;
import java.util.ArrayList;

public class Organization_Employee  {

    private String Name;
    private String EmpID;
    private String Address;





    private List<Organization_Skill> organization_skills;


    public Organization_Employee(
        String Name,        String EmpID,        String Address    ) {
        this.Name = Name;
        this.EmpID = EmpID;
        this.Address = Address;
        this.organization_skills = new ArrayList<>();
    }

    public Organization_Employee(
        String Name,        String EmpID,        String Address        ArrayList<Organization_Skill> organization_skills    ) {
        this.Name = Name;
        this.EmpID = EmpID;
        this.Address = Address;
        this.organization_skills = organization_skills;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getEmpid() {
        return EmpID;
    }

    public void setEmpid(String EmpID) {
        this.EmpID = EmpID;
    }
    public String getAddress() {
        return Address;
    }

    public void setAddress(String Address) {
        this.Address = Address;
    }

    public List<Organization_Skill> getOrganization_skills() {
        return organization_skills;
    }

    public void addOrganization_skill(Organization_skill organization_skill) {
        this.organization_skills.add(organization_skill);
    }

}