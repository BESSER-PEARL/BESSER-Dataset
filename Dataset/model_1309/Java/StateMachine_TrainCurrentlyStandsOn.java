





import java.util.List;
import java.util.ArrayList;

public class StateMachine_TrainCurrentlyStandsOn extends GuardExpression {






    private List<StateMachine_TrackElement> statemachine_trackelements;




    private StateMachine_Train statemachine_train;


    public StateMachine_TrainCurrentlyStandsOn(
    ) {
        super(
        );
        this.statemachine_trackelements = new ArrayList<>();
    }

    public StateMachine_TrainCurrentlyStandsOn(
        ArrayList<StateMachine_TrackElement> statemachine_trackelements    ) {
        this.statemachine_trackelements = statemachine_trackelements;
    }


    public List<StateMachine_TrackElement> getStatemachine_trackelements() {
        return statemachine_trackelements;
    }

    public void addStatemachine_trackelement(Statemachine_trackelement statemachine_trackelement) {
        this.statemachine_trackelements.add(statemachine_trackelement);
    }
    public StateMachine_Train getStatemachine_train() {
        return statemachine_train;
    }

    public void setStatemachine_train(StateMachine_Train statemachine_train) {
        this.statemachine_train = statemachine_train;
    }

}