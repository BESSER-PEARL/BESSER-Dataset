





import java.util.List;
import java.util.ArrayList;

public class libraryElement_Primitive  {

    private String event;
    private String parameters;





    private libraryElement_ServiceInterface libraryelement_serviceinterface;


    public libraryElement_Primitive(
        String event,        String parameters    ) {
        this.event = event;
        this.parameters = parameters;
    }


    public String getEvent() {
        return event;
    }

    public void setEvent(String event) {
        this.event = event;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public libraryElement_ServiceInterface getLibraryelement_serviceinterface() {
        return libraryelement_serviceinterface;
    }

    public void setLibraryelement_serviceinterface(libraryElement_ServiceInterface libraryelement_serviceinterface) {
        this.libraryelement_serviceinterface = libraryelement_serviceinterface;
    }

}