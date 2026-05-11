





import java.util.List;
import java.util.ArrayList;

public class contentfwk_Objective extends Element {






    private contentfwk_Objective contentfwk_objective;




    private contentfwk_Goal contentfwk_goal;




    private contentfwk_BusinessArchitecture contentfwk_businessarchitecture;




    private List<contentfwk_Goal> contentfwk_goals;


    public contentfwk_Objective(
    ) {
        super(
        );
        this.contentfwk_goals = new ArrayList<>();
    }

    public contentfwk_Objective(
        ArrayList<contentfwk_Goal> contentfwk_goals    ) {
        this.contentfwk_goals = contentfwk_goals;
    }


    public contentfwk_Objective getContentfwk_objective() {
        return contentfwk_objective;
    }

    public void setContentfwk_objective(contentfwk_Objective contentfwk_objective) {
        this.contentfwk_objective = contentfwk_objective;
    }
    public contentfwk_Goal getContentfwk_goal() {
        return contentfwk_goal;
    }

    public void setContentfwk_goal(contentfwk_Goal contentfwk_goal) {
        this.contentfwk_goal = contentfwk_goal;
    }
    public contentfwk_BusinessArchitecture getContentfwk_businessarchitecture() {
        return contentfwk_businessarchitecture;
    }

    public void setContentfwk_businessarchitecture(contentfwk_BusinessArchitecture contentfwk_businessarchitecture) {
        this.contentfwk_businessarchitecture = contentfwk_businessarchitecture;
    }
    public List<contentfwk_Goal> getContentfwk_goals() {
        return contentfwk_goals;
    }

    public void addContentfwk_goal(Contentfwk_goal contentfwk_goal) {
        this.contentfwk_goals.add(contentfwk_goal);
    }

}