





import java.util.List;
import java.util.ArrayList;

public class tfsm_FSMClock extends NamedElement {

    private int numberOfTicks;



    public tfsm_FSMClock(
        int numberOfTicks    ) {
        super(
        );
        this.numberOfTicks = numberOfTicks;
    }


    public int getNumberofticks() {
        return numberOfTicks;
    }

    public void setNumberofticks(int numberOfTicks) {
        this.numberOfTicks = numberOfTicks;
    }


}