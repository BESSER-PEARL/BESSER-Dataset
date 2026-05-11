





import java.util.List;
import java.util.ArrayList;

public class exo1_Departement  {

    private String name;
    private int budget;
    private String location;





    private exo1_Company exo1_company;


    public exo1_Departement(
        String name,        int budget,        String location    ) {
        this.name = name;
        this.budget = budget;
        this.location = location;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getBudget() {
        return budget;
    }

    public void setBudget(int budget) {
        this.budget = budget;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public exo1_Company getExo1_company() {
        return exo1_company;
    }

    public void setExo1_company(exo1_Company exo1_company) {
        this.exo1_company = exo1_company;
    }

}