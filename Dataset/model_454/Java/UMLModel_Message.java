





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Message extends NamedElement {

    private String connector;
    private String signature;
    private String sendEvent;
    private String interaction;
    private String receiveEvent;
    private String messageKind;
    private String messageSort;





    private List<UMLModel_ValueSpecification> umlmodel_valuespecifications;




    private UMLModel_Interaction umlmodel_interaction;


    public UMLModel_Message(
        String connector,        String signature,        String sendEvent,        String interaction,        String receiveEvent,        String messageKind,        String messageSort    ) {
        super(
        );
        this.connector = connector;
        this.signature = signature;
        this.sendEvent = sendEvent;
        this.interaction = interaction;
        this.receiveEvent = receiveEvent;
        this.messageKind = messageKind;
        this.messageSort = messageSort;
        this.umlmodel_valuespecifications = new ArrayList<>();
    }

    public UMLModel_Message(
        String connector,        String signature,        String sendEvent,        String interaction,        String receiveEvent,        String messageKind,        String messageSort        ArrayList<UMLModel_ValueSpecification> umlmodel_valuespecifications    ) {
        this.connector = connector;
        this.signature = signature;
        this.sendEvent = sendEvent;
        this.interaction = interaction;
        this.receiveEvent = receiveEvent;
        this.messageKind = messageKind;
        this.messageSort = messageSort;
        this.umlmodel_valuespecifications = umlmodel_valuespecifications;
    }

    public String getConnector() {
        return connector;
    }

    public void setConnector(String connector) {
        this.connector = connector;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }
    public String getSendevent() {
        return sendEvent;
    }

    public void setSendevent(String sendEvent) {
        this.sendEvent = sendEvent;
    }
    public String getInteraction() {
        return interaction;
    }

    public void setInteraction(String interaction) {
        this.interaction = interaction;
    }
    public String getReceiveevent() {
        return receiveEvent;
    }

    public void setReceiveevent(String receiveEvent) {
        this.receiveEvent = receiveEvent;
    }
    public String getMessagekind() {
        return messageKind;
    }

    public void setMessagekind(String messageKind) {
        this.messageKind = messageKind;
    }
    public String getMessagesort() {
        return messageSort;
    }

    public void setMessagesort(String messageSort) {
        this.messageSort = messageSort;
    }

    public List<UMLModel_ValueSpecification> getUmlmodel_valuespecifications() {
        return umlmodel_valuespecifications;
    }

    public void addUmlmodel_valuespecification(Umlmodel_valuespecification umlmodel_valuespecification) {
        this.umlmodel_valuespecifications.add(umlmodel_valuespecification);
    }
    public UMLModel_Interaction getUmlmodel_interaction() {
        return umlmodel_interaction;
    }

    public void setUmlmodel_interaction(UMLModel_Interaction umlmodel_interaction) {
        this.umlmodel_interaction = umlmodel_interaction;
    }

}