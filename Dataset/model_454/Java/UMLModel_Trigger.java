





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Trigger extends NamedElement {

    private String port;
    private String event;





    private UMLModel_AcceptEventAction umlmodel_accepteventaction;




    private UMLModel_State umlmodel_state;


    public UMLModel_Trigger(
        String port,        String event    ) {
        super(
        );
        this.port = port;
        this.event = event;
    }


    public String getPort() {
        return port;
    }

    public void setPort(String port) {
        this.port = port;
    }
    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }

    public UMLModel_AcceptEventAction getUmlmodel_accepteventaction() {
        return umlmodel_accepteventaction;
    }

    public void setUmlmodel_accepteventaction(UMLModel_AcceptEventAction umlmodel_accepteventaction) {
        this.umlmodel_accepteventaction = umlmodel_accepteventaction;
    }
    public UMLModel_State getUmlmodel_state() {
        return umlmodel_state;
    }

    public void setUmlmodel_state(UMLModel_State umlmodel_state) {
        this.umlmodel_state = umlmodel_state;
    }

}