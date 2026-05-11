





import java.util.List;
import java.util.ArrayList;

public class mdc_StationaryState extends State {






    private List<mdc_State> mdc_states;




    private mdc_Chatbot mdc_chatbot;


    public mdc_StationaryState(
    ) {
        super(
        );
        this.mdc_states = new ArrayList<>();
    }

    public mdc_StationaryState(
        ArrayList<mdc_State> mdc_states    ) {
        this.mdc_states = mdc_states;
    }


    public List<mdc_State> getMdc_states() {
        return mdc_states;
    }

    public void addMdc_state(Mdc_state mdc_state) {
        this.mdc_states.add(mdc_state);
    }
    public mdc_Chatbot getMdc_chatbot() {
        return mdc_chatbot;
    }

    public void setMdc_chatbot(mdc_Chatbot mdc_chatbot) {
        this.mdc_chatbot = mdc_chatbot;
    }

}