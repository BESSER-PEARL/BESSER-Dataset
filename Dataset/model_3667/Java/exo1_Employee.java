





import java.util.List;
import java.util.ArrayList;

public class exo1_Employee  {

    private String salary;
    private String name;





    private exo1_Project exo1_project;




    private List<exo1_Departement> exo1_departements;




    private List<exo1_Project> exo1_projects;




    private exo1_Departement exo1_departement;


    public exo1_Employee(
        String salary,        String name    ) {
        this.salary = salary;
        this.name = name;
        this.exo1_departements = new ArrayList<>();
        this.exo1_projects = new ArrayList<>();
    }

    public exo1_Employee(
        String salary,        String name        ArrayList<exo1_Departement> exo1_departements,        ArrayList<exo1_Project> exo1_projects    ) {
        this.salary = salary;
        this.name = name;
        this.exo1_departements = exo1_departements;
        this.exo1_projects = exo1_projects;
    }

    public String getSalary() {
        return salary;
    }

    public void setSalary(String salary) {
        this.salary = salary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public exo1_Project getExo1_project() {
        return exo1_project;
    }

    public void setExo1_project(exo1_Project exo1_project) {
        this.exo1_project = exo1_project;
    }
    public List<exo1_Departement> getExo1_departements() {
        return exo1_departements;
    }

    public void addExo1_departement(Exo1_departement exo1_departement) {
        this.exo1_departements.add(exo1_departement);
    }
    public List<exo1_Project> getExo1_projects() {
        return exo1_projects;
    }

    public void addExo1_project(Exo1_project exo1_project) {
        this.exo1_projects.add(exo1_project);
    }
    public exo1_Departement getExo1_departement() {
        return exo1_departement;
    }

    public void setExo1_departement(exo1_Departement exo1_departement) {
        this.exo1_departement = exo1_departement;
    }

}