





import java.util.List;
import java.util.ArrayList;

public class esper2Maude_Every  {

    private String eventVariable;
    private String eventName;





    private esper2Maude_FilterFrom esper2maude_filterfrom;




    private esper2Maude_FilterEvent esper2maude_filterevent;




    private esper2Maude_SubFilterFollowedBy esper2maude_subfilterfollowedby;


    public esper2Maude_Every(
        String eventVariable,        String eventName    ) {
        this.eventVariable = eventVariable;
        this.eventName = eventName;
    }


    public String getEventvariable() {
        return eventVariable;
    }

    public void setEventvariable(String eventVariable) {
        this.eventVariable = eventVariable;
    }
    public String getEventname() {
        return eventName;
    }

    public void setEventname(String eventName) {
        this.eventName = eventName;
    }

    public esper2Maude_FilterFrom getEsper2maude_filterfrom() {
        return esper2maude_filterfrom;
    }

    public void setEsper2maude_filterfrom(esper2Maude_FilterFrom esper2maude_filterfrom) {
        this.esper2maude_filterfrom = esper2maude_filterfrom;
    }
    public esper2Maude_FilterEvent getEsper2maude_filterevent() {
        return esper2maude_filterevent;
    }

    public void setEsper2maude_filterevent(esper2Maude_FilterEvent esper2maude_filterevent) {
        this.esper2maude_filterevent = esper2maude_filterevent;
    }
    public esper2Maude_SubFilterFollowedBy getEsper2maude_subfilterfollowedby() {
        return esper2maude_subfilterfollowedby;
    }

    public void setEsper2maude_subfilterfollowedby(esper2Maude_SubFilterFollowedBy esper2maude_subfilterfollowedby) {
        this.esper2maude_subfilterfollowedby = esper2maude_subfilterfollowedby;
    }

}