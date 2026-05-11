





import java.util.List;
import java.util.ArrayList;

public class prosjekt_University  {

    private String shortName;
    private String name;





    private prosjekt_Department prosjekt_department;




    private List<prosjekt_Department> prosjekt_departments;


    public prosjekt_University(
        String shortName,        String name    ) {
        this.shortName = shortName;
        this.name = name;
        this.prosjekt_departments = new ArrayList<>();
    }

    public prosjekt_University(
        String shortName,        String name        ArrayList<prosjekt_Department> prosjekt_departments    ) {
        this.shortName = shortName;
        this.name = name;
        this.prosjekt_departments = prosjekt_departments;
    }

    public String getShortname() {
        return shortName;
    }

    public void setShortname(String shortName) {
        this.shortName = shortName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public prosjekt_Department getProsjekt_department() {
        return prosjekt_department;
    }

    public void setProsjekt_department(prosjekt_Department prosjekt_department) {
        this.prosjekt_department = prosjekt_department;
    }
    public List<prosjekt_Department> getProsjekt_departments() {
        return prosjekt_departments;
    }

    public void addProsjekt_department(Prosjekt_department prosjekt_department) {
        this.prosjekt_departments.add(prosjekt_department);
    }

}