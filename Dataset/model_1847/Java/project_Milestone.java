





import java.util.List;
import java.util.ArrayList;

public class project_Milestone extends TaskAttribute {

    private boolean milestone;



    public project_Milestone(
        boolean milestone    ) {
        super(
        );
        this.milestone = milestone;
    }


    public boolean getMilestone() {
        return milestone;
    }

    public void setMilestone(boolean milestone) {
        this.milestone = milestone;
    }


}