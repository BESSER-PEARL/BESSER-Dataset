





import java.util.List;
import java.util.ArrayList;

public class shr5Management_TrainingsTime extends CharacterChange {

    private int daysRemains;
    private int daysTrained;
    private boolean trainingComplete;



    public shr5Management_TrainingsTime(
        int daysRemains,        int daysTrained,        boolean trainingComplete    ) {
        super(
        );
        this.daysRemains = daysRemains;
        this.daysTrained = daysTrained;
        this.trainingComplete = trainingComplete;
    }


    public int getDaysremains() {
        return daysRemains;
    }

    public void setDaysremains(int daysRemains) {
        this.daysRemains = daysRemains;
    }
    public int getDaystrained() {
        return daysTrained;
    }

    public void setDaystrained(int daysTrained) {
        this.daysTrained = daysTrained;
    }
    public boolean getTrainingcomplete() {
        return trainingComplete;
    }

    public void setTrainingcomplete(boolean trainingComplete) {
        this.trainingComplete = trainingComplete;
    }


}