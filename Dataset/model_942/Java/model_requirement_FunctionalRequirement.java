





import java.util.List;
import java.util.ArrayList;

public class model_requirement_FunctionalRequirement extends UnicaseModelElement {

    private boolean reviewed;
    private int cost;
    private int storyPoints;
    private int priority;



    public model_requirement_FunctionalRequirement(
        boolean reviewed,        int cost,        int storyPoints,        int priority    ) {
        super(
        );
        this.reviewed = reviewed;
        this.cost = cost;
        this.storyPoints = storyPoints;
        this.priority = priority;
    }


    public boolean getReviewed() {
        return reviewed;
    }

    public void setReviewed(boolean reviewed) {
        this.reviewed = reviewed;
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
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }


}