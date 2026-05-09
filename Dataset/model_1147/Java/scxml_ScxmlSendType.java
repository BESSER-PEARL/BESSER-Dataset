





import java.util.List;
import java.util.ArrayList;

public class scxml_ScxmlSendType  {

    private String event;





    private scxml_ScxmlOnexecuteType scxml_scxmlonexecutetype;


    public scxml_ScxmlSendType(
        String event    ) {
        this.event = event;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public scxml_ScxmlOnexecuteType getScxml_scxmlonexecutetype() {
        return scxml_scxmlonexecutetype;
    }

    public void setScxml_scxmlonexecutetype(scxml_ScxmlOnexecuteType scxml_scxmlonexecutetype) {
        this.scxml_scxmlonexecutetype = scxml_scxmlonexecutetype;
    }

}