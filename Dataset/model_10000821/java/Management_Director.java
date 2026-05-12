





import java.util.List;
import java.util.ArrayList;

public class Management_Director  {

    private float budget;





    private Management_DirectorTest management_directortest;


    public Management_Director(
        float budget    ) {
        this.budget = budget;
    }


    public float getBudget() {
        return budget;
    }

    public void setBudget(float budget) {
        this.budget = budget;
    }

    public Management_DirectorTest getManagement_directortest() {
        return management_directortest;
    }

    public void setManagement_directortest(Management_DirectorTest management_directortest) {
        this.management_directortest = management_directortest;
    }

}