





import java.util.List;
import java.util.ArrayList;

public class exo1_Employee  {

    private String name;
    private String salary;





    private List<exo1_Departement> exo1_departements;




    private exo1_Company exo1_company;




    private List<exo1_Project> exo1_projects;




    private exo1_Project exo1_project;




    private exo1_Departement exo1_departement;


    public exo1_Employee(
        String name,        String salary    ) {
        this.name = name;
        this.salary = salary;
        this.exo1_departements = new ArrayList<>();
        this.exo1_projects = new ArrayList<>();
    }

    public exo1_Employee(
        String name,        String salary        ArrayList<exo1_Departement> exo1_departements,        ArrayList<exo1_Project> exo1_projects    ) {
        this.name = name;
        this.salary = salary;
        this.exo1_departements = exo1_departements;
        this.exo1_projects = exo1_projects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSalary() {
        return salary;
    }

    public void setSalary(String salary) {
        this.salary = salary;
    }

    public List<exo1_Departement> getExo1_departements() {
        return exo1_departements;
    }

    public void addExo1_departement(Exo1_departement exo1_departement) {
        this.exo1_departements.add(exo1_departement);
    }
    public exo1_Company getExo1_company() {
        return exo1_company;
    }

    public void setExo1_company(exo1_Company exo1_company) {
        this.exo1_company = exo1_company;
    }
    public List<exo1_Project> getExo1_projects() {
        return exo1_projects;
    }

    public void addExo1_project(Exo1_project exo1_project) {
        this.exo1_projects.add(exo1_project);
    }
    public exo1_Project getExo1_project() {
        return exo1_project;
    }

    public void setExo1_project(exo1_Project exo1_project) {
        this.exo1_project = exo1_project;
    }
    public exo1_Departement getExo1_departement() {
        return exo1_departement;
    }

    public void setExo1_departement(exo1_Departement exo1_departement) {
        this.exo1_departement = exo1_departement;
    }

}