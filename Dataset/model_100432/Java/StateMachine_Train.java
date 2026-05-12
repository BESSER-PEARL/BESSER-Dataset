





import java.util.List;
import java.util.ArrayList;

public class StateMachine_Train  {






    private StateMachine_ChangeTrainCurrentTrackElement statemachine_changetraincurrenttrackelement;




    private StateMachine_ChangeTrainHeadingSpeed statemachine_changetrainheadingspeed;


    public StateMachine_Train(
    ) {
    }



    public StateMachine_ChangeTrainCurrentTrackElement getStatemachine_changetraincurrenttrackelement() {
        return statemachine_changetraincurrenttrackelement;
    }

    public void setStatemachine_changetraincurrenttrackelement(StateMachine_ChangeTrainCurrentTrackElement statemachine_changetraincurrenttrackelement) {
        this.statemachine_changetraincurrenttrackelement = statemachine_changetraincurrenttrackelement;
    }
    public StateMachine_ChangeTrainHeadingSpeed getStatemachine_changetrainheadingspeed() {
        return statemachine_changetrainheadingspeed;
    }

    public void setStatemachine_changetrainheadingspeed(StateMachine_ChangeTrainHeadingSpeed statemachine_changetrainheadingspeed) {
        this.statemachine_changetrainheadingspeed = statemachine_changetrainheadingspeed;
    }

}