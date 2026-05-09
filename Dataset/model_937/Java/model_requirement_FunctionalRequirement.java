





import java.util.List;
import java.util.ArrayList;

public class model_requirement_FunctionalRequirement extends UnicaseModelElement {

    private int storyPoints;
    private int cost;
    private int priority;
    private boolean reviewed;



    public model_requirement_FunctionalRequirement(
        int storyPoints,        int cost,        int priority,        boolean reviewed    ) {
        super(
        );
        this.storyPoints = storyPoints;
        this.cost = cost;
        this.priority = priority;
        this.reviewed = reviewed;
    }


    public int getStorypoints() {
        return storyPoints;
    }

    public void setStorypoints(int storyPoints) {
        this.storyPoints = storyPoints;
    }
    public int getCost() {
        return cost;
    }

    public void setCost(int cost) {
        this.cost = cost;
    }
    public int getPriority() {
        return priority;
    }

    public void setPriority(int priority) {
        this.priority = priority;
    }
    public boolean getReviewed() {
        return reviewed;
    }

    public void setReviewed(boolean reviewed) {
        this.reviewed = reviewed;
    }


}