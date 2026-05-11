





import java.util.List;
import java.util.ArrayList;

public class oving4_Evaluation  {

    private String description;
    private float creditsReceived;
    private boolean completed;
    private float totalPercentageResult;



    public oving4_Evaluation(
        String description,        float creditsReceived,        boolean completed,        float totalPercentageResult    ) {
        this.description = description;
        this.creditsReceived = creditsReceived;
        this.completed = completed;
        this.totalPercentageResult = totalPercentageResult;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public float getCreditsreceived() {
        return creditsReceived;
    }

    public void setCreditsreceived(float creditsReceived) {
        this.creditsReceived = creditsReceived;
    }
    public boolean getCompleted() {
        return completed;
    }

    public void setCompleted(boolean completed) {
        this.completed = completed;
    }
    public float getTotalpercentageresult() {
        return totalPercentageResult;
    }

    public void setTotalpercentageresult(float totalPercentageResult) {
        this.totalPercentageResult = totalPercentageResult;
    }


}