





import java.util.List;
import java.util.ArrayList;

public class scxml_CondEventTransition extends Transition {

    private String cond;
    private String event;





    private scxml_TransitionSource scxml_transitionsource;


    public scxml_CondEventTransition(
        String cond,        String event    ) {
        super(
        );
        this.cond = cond;
        this.event = event;
    }


    public String getCond() {
        return cond;
    }

    public void setCond(String cond) {
        this.cond = cond;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public scxml_TransitionSource getScxml_transitionsource() {
        return scxml_transitionsource;
    }

    public void setScxml_transitionsource(scxml_TransitionSource scxml_transitionsource) {
        this.scxml_transitionsource = scxml_transitionsource;
    }

}