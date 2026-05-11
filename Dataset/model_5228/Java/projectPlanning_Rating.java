





import java.util.List;
import java.util.ArrayList;

public class projectPlanning_Rating  {

    private int rating;





    private projectPlanning_Capability projectplanning_capability;




    private projectPlanning_ProjectPlan projectplanning_projectplan;




    private projectPlanning_Employee projectplanning_employee;


    public projectPlanning_Rating(
        int rating    ) {
        this.rating = rating;
    }


    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }

    public projectPlanning_Capability getProjectplanning_capability() {
        return projectplanning_capability;
    }

    public void setProjectplanning_capability(projectPlanning_Capability projectplanning_capability) {
        this.projectplanning_capability = projectplanning_capability;
    }
    public projectPlanning_ProjectPlan getProjectplanning_projectplan() {
        return projectplanning_projectplan;
    }

    public void setProjectplanning_projectplan(projectPlanning_ProjectPlan projectplanning_projectplan) {
        this.projectplanning_projectplan = projectplanning_projectplan;
    }
    public projectPlanning_Employee getProjectplanning_employee() {
        return projectplanning_employee;
    }

    public void setProjectplanning_employee(projectPlanning_Employee projectplanning_employee) {
        this.projectplanning_employee = projectplanning_employee;
    }

}