





import java.util.List;
import java.util.ArrayList;

public class exo1_Company  {






    private List<exo1_Project> exo1_projects;




    private List<exo1_Employee> exo1_employees;




    private List<exo1_Departement> exo1_departements;


    public exo1_Company(
    ) {
        this.exo1_projects = new ArrayList<>();
        this.exo1_employees = new ArrayList<>();
        this.exo1_departements = new ArrayList<>();
    }

    public exo1_Company(
        ArrayList<exo1_Project> exo1_projects,        ArrayList<exo1_Employee> exo1_employees,        ArrayList<exo1_Departement> exo1_departements    ) {
        this.exo1_projects = exo1_projects;
        this.exo1_employees = exo1_employees;
        this.exo1_departements = exo1_departements;
    }


    public List<exo1_Project> getExo1_projects() {
        return exo1_projects;
    }

    public void addExo1_project(Exo1_project exo1_project) {
        this.exo1_projects.add(exo1_project);
    }
    public List<exo1_Employee> getExo1_employees() {
        return exo1_employees;
    }

    public void addExo1_employee(Exo1_employee exo1_employee) {
        this.exo1_employees.add(exo1_employee);
    }
    public List<exo1_Departement> getExo1_departements() {
        return exo1_departements;
    }

    public void addExo1_departement(Exo1_departement exo1_departement) {
        this.exo1_departements.add(exo1_departement);
    }

}