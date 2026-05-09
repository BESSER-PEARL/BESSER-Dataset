





import java.util.List;
import java.util.ArrayList;

public class martinfowlerdsl_StateMachine  {






    private List<martinfowlerdsl_AbstractEvent> martinfowlerdsl_abstractevents;


    public martinfowlerdsl_StateMachine(
    ) {
        this.martinfowlerdsl_abstractevents = new ArrayList<>();
    }

    public martinfowlerdsl_StateMachine(
        ArrayList<martinfowlerdsl_AbstractEvent> martinfowlerdsl_abstractevents    ) {
        this.martinfowlerdsl_abstractevents = martinfowlerdsl_abstractevents;
    }


    public List<martinfowlerdsl_AbstractEvent> getMartinfowlerdsl_abstractevents() {
        return martinfowlerdsl_abstractevents;
    }

    public void addMartinfowlerdsl_abstractevent(Martinfowlerdsl_abstractevent martinfowlerdsl_abstractevent) {
        this.martinfowlerdsl_abstractevents.add(martinfowlerdsl_abstractevent);
    }

}