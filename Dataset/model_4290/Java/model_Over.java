





import java.util.List;
import java.util.ArrayList;

public class model_Over  {

    private int runs;
    private int validBalls;
    private int BALLS_IN_OVER;
    private boolean isComplete;





    private model_Innings model_innings;




    private model_Innings model_innings;


    public model_Over(
        int runs,        int validBalls,        int BALLS_IN_OVER,        boolean isComplete    ) {
        this.runs = runs;
        this.validBalls = validBalls;
        this.BALLS_IN_OVER = BALLS_IN_OVER;
        this.isComplete = isComplete;
    }


    public int getRuns() {
        return runs;
    }

    public void setRuns(int runs) {
        this.runs = runs;
    }
    public int getValidballs() {
        return validBalls;
    }

    public void setValidballs(int validBalls) {
        this.validBalls = validBalls;
    }
    public int getBalls_in_over() {
        return BALLS_IN_OVER;
    }

    public void setBalls_in_over(int BALLS_IN_OVER) {
        this.BALLS_IN_OVER = BALLS_IN_OVER;
    }
    public boolean getIscomplete() {
        return isComplete;
    }

    public void setIscomplete(boolean isComplete) {
        this.isComplete = isComplete;
    }

    public model_Innings getModel_innings() {
        return model_innings;
    }

    public void setModel_innings(model_Innings model_innings) {
        this.model_innings = model_innings;
    }
    public model_Innings getModel_innings() {
        return model_innings;
    }

    public void setModel_innings(model_Innings model_innings) {
        this.model_innings = model_innings;
    }

}