





import java.util.List;
import java.util.ArrayList;

public class mmb_Transition  {

    private String Event;





    private mmb_Automaton mmb_automaton;




    private mmb_Mode mmb_mode;




    private mmb_Mode mmb_mode;


    public mmb_Transition(
        String Event    ) {
        this.Event = Event;
    }


    public String getEvent() {
        return Event;
    }

    public void setEvent(String Event) {
        this.Event = Event;
    }

    public mmb_Automaton getMmb_automaton() {
        return mmb_automaton;
    }

    public void setMmb_automaton(mmb_Automaton mmb_automaton) {
        this.mmb_automaton = mmb_automaton;
    }
    public mmb_Mode getMmb_mode() {
        return mmb_mode;
    }

    public void setMmb_mode(mmb_Mode mmb_mode) {
        this.mmb_mode = mmb_mode;
    }
    public mmb_Mode getMmb_mode() {
        return mmb_mode;
    }

    public void setMmb_mode(mmb_Mode mmb_mode) {
        this.mmb_mode = mmb_mode;
    }

}