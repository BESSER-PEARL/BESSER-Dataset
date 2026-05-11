




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class employee_LargeProject extends Project {

    private LocalDate milestone;
    private float budget;



    public employee_LargeProject(
        LocalDate milestone,        float budget    ) {
        super(
        );
        this.milestone = milestone;
        this.budget = budget;
    }


    public LocalDate getMilestone() {
        return milestone;
    }

    public void setMilestone(LocalDate milestone) {
        this.milestone = milestone;
    }
    public float getBudget() {
        return budget;
    }

    public void setBudget(float budget) {
        this.budget = budget;
    }


}