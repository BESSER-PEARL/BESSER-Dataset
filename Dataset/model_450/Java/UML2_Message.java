





import java.util.List;
import java.util.ArrayList;

public class UML2_Message extends NamedElement {

    private String messageSort;
    private String messageKind;





    private UML2_Interaction uml2_interaction;




    private UML2_Interaction uml2_interaction;




    private UML2_Connector uml2_connector;


    public UML2_Message(
        String messageSort,        String messageKind    ) {
        super(
        );
        this.messageSort = messageSort;
        this.messageKind = messageKind;
    }


    public String getMessagesort() {
        return messageSort;
    }

    public void setMessagesort(String messageSort) {
        this.messageSort = messageSort;
    }
    public String getMessagekind() {
        return messageKind;
    }

    public void setMessagekind(String messageKind) {
        this.messageKind = messageKind;
    }

    public UML2_Interaction getUml2_interaction() {
        return uml2_interaction;
    }

    public void setUml2_interaction(UML2_Interaction uml2_interaction) {
        this.uml2_interaction = uml2_interaction;
    }
    public UML2_Interaction getUml2_interaction() {
        return uml2_interaction;
    }

    public void setUml2_interaction(UML2_Interaction uml2_interaction) {
        this.uml2_interaction = uml2_interaction;
    }
    public UML2_Connector getUml2_connector() {
        return uml2_connector;
    }

    public void setUml2_connector(UML2_Connector uml2_connector) {
        this.uml2_connector = uml2_connector;
    }

}