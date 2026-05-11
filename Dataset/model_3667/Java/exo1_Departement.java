





import java.util.List;
import java.util.ArrayList;

public class exo1_Departement  {

    private int budget;
    private String location;
    private String name;



    public exo1_Departement(
        int budget,        String location,        String name    ) {
        this.budget = budget;
        this.location = location;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}