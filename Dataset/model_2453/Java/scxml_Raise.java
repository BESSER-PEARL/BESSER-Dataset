





import java.util.List;
import java.util.ArrayList;

public class scxml_Raise  {

    private String event;





    private scxml_If scxml_if;


    public scxml_Raise(
        String event    ) {
        this.event = event;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public scxml_If getScxml_if() {
        return scxml_if;
    }

    public void setScxml_if(scxml_If scxml_if) {
        this.scxml_if = scxml_if;
    }

}