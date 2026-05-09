





import java.util.List;
import java.util.ArrayList;

public class sam_MacroState extends AbstractState {






    private sam_AbstractState sam_abstractstate;




    private List<sam_AbstractState> sam_abstractstates;


    public sam_MacroState(
    ) {
        super(
        );
        this.sam_abstractstates = new ArrayList<>();
    }

    public sam_MacroState(
        ArrayList<sam_AbstractState> sam_abstractstates    ) {
        this.sam_abstractstates = sam_abstractstates;
    }


    public sam_AbstractState getSam_abstractstate() {
        return sam_abstractstate;
    }

    public void setSam_abstractstate(sam_AbstractState sam_abstractstate) {
        this.sam_abstractstate = sam_abstractstate;
    }
    public List<sam_AbstractState> getSam_abstractstates() {
        return sam_abstractstates;
    }

    public void addSam_abstractstate(Sam_abstractstate sam_abstractstate) {
        this.sam_abstractstates.add(sam_abstractstate);
    }

}