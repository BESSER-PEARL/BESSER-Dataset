





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageTransmission extends RepositoryConcept {

    private String messageTypeDescription;





    private iso20022_Receive iso20022_receive;




    private iso20022_Send iso20022_send;




    private iso20022_MessageDefinition iso20022_messagedefinition;




    private iso20022_Send iso20022_send;




    private List<iso20022_Receive> iso20022_receives;




    private List<iso20022_MessageDefinition> iso20022_messagedefinitions;


    public iso20022_MessageTransmission(
        String messageTypeDescription    ) {
        super(
        );
        this.messageTypeDescription = messageTypeDescription;
        this.iso20022_receives = new ArrayList<>();
        this.iso20022_messagedefinitions = new ArrayList<>();
    }

    public iso20022_MessageTransmission(
        String messageTypeDescription        ArrayList<iso20022_Receive> iso20022_receives,        ArrayList<iso20022_MessageDefinition> iso20022_messagedefinitions    ) {
        this.messageTypeDescription = messageTypeDescription;
        this.iso20022_receives = iso20022_receives;
        this.iso20022_messagedefinitions = iso20022_messagedefinitions;
    }

    public String getMessagetypedescription() {
        return messageTypeDescription;
    }

    public void setMessagetypedescription(String messageTypeDescription) {
        this.messageTypeDescription = messageTypeDescription;
    }

    public iso20022_Receive getIso20022_receive() {
        return iso20022_receive;
    }

    public void setIso20022_receive(iso20022_Receive iso20022_receive) {
        this.iso20022_receive = iso20022_receive;
    }
    public iso20022_Send getIso20022_send() {
        return iso20022_send;
    }

    public void setIso20022_send(iso20022_Send iso20022_send) {
        this.iso20022_send = iso20022_send;
    }
    public iso20022_MessageDefinition getIso20022_messagedefinition() {
        return iso20022_messagedefinition;
    }

    public void setIso20022_messagedefinition(iso20022_MessageDefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinition = iso20022_messagedefinition;
    }
    public iso20022_Send getIso20022_send() {
        return iso20022_send;
    }

    public void setIso20022_send(iso20022_Send iso20022_send) {
        this.iso20022_send = iso20022_send;
    }
    public List<iso20022_Receive> getIso20022_receives() {
        return iso20022_receives;
    }

    public void addIso20022_receive(Iso20022_receive iso20022_receive) {
        this.iso20022_receives.add(iso20022_receive);
    }
    public List<iso20022_MessageDefinition> getIso20022_messagedefinitions() {
        return iso20022_messagedefinitions;
    }

    public void addIso20022_messagedefinition(Iso20022_messagedefinition iso20022_messagedefinition) {
        this.iso20022_messagedefinitions.add(iso20022_messagedefinition);
    }

}