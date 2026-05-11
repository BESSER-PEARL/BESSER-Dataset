





import java.util.List;
import java.util.ArrayList;

public class esper2Maude_SubFilterFollowedBy  {

    private String eventName;
    private String eventVariable;





    private esper2Maude_FilterEvent esper2maude_filterevent;


    public esper2Maude_SubFilterFollowedBy(
        String eventName,        String eventVariable    ) {
        this.eventName = eventName;
        this.eventVariable = eventVariable;
    }


    public String getEventname() {
        return eventName;
    }

    public void setEventname(String eventName) {
        this.eventName = eventName;
    }
    public String getEventvariable() {
        return eventVariable;
    }

    public void setEventvariable(String eventVariable) {
        this.eventVariable = eventVariable;
    }

    public esper2Maude_FilterEvent getEsper2maude_filterevent() {
        return esper2maude_filterevent;
    }

    public void setEsper2maude_filterevent(esper2Maude_FilterEvent esper2maude_filterevent) {
        this.esper2maude_filterevent = esper2maude_filterevent;
    }

}