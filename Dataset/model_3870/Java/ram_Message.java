





import java.util.List;
import java.util.ArrayList;

public class ram_Message  {

    private boolean selfMessage;
    private String messageSort;





    private ram_Interaction ram_interaction;




    private ram_StructuralFeature ram_structuralfeature;




    private ram_Interaction ram_interaction;




    private ram_Operation ram_operation;


    public ram_Message(
        boolean selfMessage,        String messageSort    ) {
        this.selfMessage = selfMessage;
        this.messageSort = messageSort;
    }


    public boolean getSelfmessage() {
        return selfMessage;
    }

    public void setSelfmessage(boolean selfMessage) {
        this.selfMessage = selfMessage;
    }
    public String getMessagesort() {
        return messageSort;
    }

    public void setMessagesort(String messageSort) {
        this.messageSort = messageSort;
    }

    public ram_Interaction getRam_interaction() {
        return ram_interaction;
    }

    public void setRam_interaction(ram_Interaction ram_interaction) {
        this.ram_interaction = ram_interaction;
    }
    public ram_StructuralFeature getRam_structuralfeature() {
        return ram_structuralfeature;
    }

    public void setRam_structuralfeature(ram_StructuralFeature ram_structuralfeature) {
        this.ram_structuralfeature = ram_structuralfeature;
    }
    public ram_Interaction getRam_interaction() {
        return ram_interaction;
    }

    public void setRam_interaction(ram_Interaction ram_interaction) {
        this.ram_interaction = ram_interaction;
    }
    public ram_Operation getRam_operation() {
        return ram_operation;
    }

    public void setRam_operation(ram_Operation ram_operation) {
        this.ram_operation = ram_operation;
    }

}