




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class employee_LargeProject extends Project {

    private float budget;
    private LocalDate milestone;



    public employee_LargeProject(
        float budget,        LocalDate milestone    ) {
        super(
        );
        this.budget = budget;
        this.milestone = milestone;
    }


    public float getBudget() {
        return budget;
    }

    public void setBudget(float budget) {
        this.budget = budget;
    }
    public LocalDate getMilestone() {
        return milestone;
    }

    public void setMilestone(LocalDate milestone) {
        this.milestone = milestone;
    }


}