





import java.util.List;
import java.util.ArrayList;

public class robochart_StateMachineBody extends NodeContainer, Context {






    private List<robochart_Clock> robochart_clocks;


    public robochart_StateMachineBody(
    ) {
        super(
        );
        this.robochart_clocks = new ArrayList<>();
    }

    public robochart_StateMachineBody(
        ArrayList<robochart_Clock> robochart_clocks    ) {
        this.robochart_clocks = robochart_clocks;
    }


    public List<robochart_Clock> getRobochart_clocks() {
        return robochart_clocks;
    }

    public void addRobochart_clock(Robochart_clock robochart_clock) {
        this.robochart_clocks.add(robochart_clock);
    }

}