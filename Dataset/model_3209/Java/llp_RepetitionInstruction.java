





import java.util.List;
import java.util.ArrayList;

public class llp_RepetitionInstruction extends ControlFlowInstruction {

    private int numberOfRepetitions;



    public llp_RepetitionInstruction(
        int numberOfRepetitions    ) {
        super(
        );
        this.numberOfRepetitions = numberOfRepetitions;
    }


    public int getNumberofrepetitions() {
        return numberOfRepetitions;
    }

    public void setNumberofrepetitions(int numberOfRepetitions) {
        this.numberOfRepetitions = numberOfRepetitions;
    }


}