





import java.util.List;
import java.util.ArrayList;

public class caltrop_Transition  {






    private List<caltrop_OutputAction> caltrop_outputactions;




    private caltrop_State caltrop_state;




    private caltrop_State caltrop_state;




    private caltrop_State caltrop_state;


    public caltrop_Transition(
    ) {
        this.caltrop_outputactions = new ArrayList<>();
    }

    public caltrop_Transition(
        ArrayList<caltrop_OutputAction> caltrop_outputactions    ) {
        this.caltrop_outputactions = caltrop_outputactions;
    }


    public List<caltrop_OutputAction> getCaltrop_outputactions() {
        return caltrop_outputactions;
    }

    public void addCaltrop_outputaction(Caltrop_outputaction caltrop_outputaction) {
        this.caltrop_outputactions.add(caltrop_outputaction);
    }
    public caltrop_State getCaltrop_state() {
        return caltrop_state;
    }

    public void setCaltrop_state(caltrop_State caltrop_state) {
        this.caltrop_state = caltrop_state;
    }
    public caltrop_State getCaltrop_state() {
        return caltrop_state;
    }

    public void setCaltrop_state(caltrop_State caltrop_state) {
        this.caltrop_state = caltrop_state;
    }
    public caltrop_State getCaltrop_state() {
        return caltrop_state;
    }

    public void setCaltrop_state(caltrop_State caltrop_state) {
        this.caltrop_state = caltrop_state;
    }

}