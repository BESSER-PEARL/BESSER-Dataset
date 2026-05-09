





import java.util.List;
import java.util.ArrayList;

public class model_requirement_FunctionalRequirement extends UnicaseModelElement {

    private int cost;
    private int storyPoints;
    private boolean reviewed;
    private int priority;



    public model_requirement_FunctionalRequirement(
        int cost,        int storyPoints,        boolean reviewed,        int priority    ) {
        super(
        );
        this.cost = cost;
        this.storyPoints = storyPoints;
        this.reviewed = reviewed;
        this.priority = priority;
    }


    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }
    public int getStorypoints() {
        return storyPoints;
    }

    public void setStorypoints(int storyPoints) {
        this.storyPoints = storyPoints;
    }
    public boolean getReviewed() {
        return reviewed;
    }

    public void setReviewed(boolean reviewed) {
        this.reviewed = reviewed;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }


}