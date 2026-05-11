





import java.util.List;
import java.util.ArrayList;

public class ram_Message  {

    private String messageSort;
    private boolean selfMessage;





    private ram_StructuralFeature ram_structuralfeature;




    private ram_Operation ram_operation;




    private ram_Interaction ram_interaction;




    private ram_MessageEnd ram_messageend;




    private ram_MessageEnd ram_messageend;




    private List<ram_ParameterValueMapping> ram_parametervaluemappings;




    private ram_MessageEnd ram_messageend;




    private ram_Interaction ram_interaction;


    public ram_Message(
        String messageSort,        boolean selfMessage    ) {
        this.messageSort = messageSort;
        this.selfMessage = selfMessage;
        this.ram_parametervaluemappings = new ArrayList<>();
    }

    public ram_Message(
        String messageSort,        boolean selfMessage        ArrayList<ram_ParameterValueMapping> ram_parametervaluemappings    ) {
        this.messageSort = messageSort;
        this.selfMessage = selfMessage;
        this.ram_parametervaluemappings = ram_parametervaluemappings;
    }

    public String getMessagesort() {
        return messageSort;
    }

    public void setMessagesort(String messageSort) {
        this.messageSort = messageSort;
    }
    public boolean getSelfmessage() {
        return selfMessage;
    }

    public void setSelfmessage(boolean selfMessage) {
        this.selfMessage = selfMessage;
    }

    public ram_StructuralFeature getRam_structuralfeature() {
        return ram_structuralfeature;
    }

    public void setRam_structuralfeature(ram_StructuralFeature ram_structuralfeature) {
        this.ram_structuralfeature = ram_structuralfeature;
    }
    public ram_Operation getRam_operation() {
        return ram_operation;
    }

    public void setRam_operation(ram_Operation ram_operation) {
        this.ram_operation = ram_operation;
    }
    public ram_Interaction getRam_interaction() {
        return ram_interaction;
    }

    public void setRam_interaction(ram_Interaction ram_interaction) {
        this.ram_interaction = ram_interaction;
    }
    public ram_MessageEnd getRam_messageend() {
        return ram_messageend;
    }

    public void setRam_messageend(ram_MessageEnd ram_messageend) {
        this.ram_messageend = ram_messageend;
    }
    public ram_MessageEnd getRam_messageend() {
        return ram_messageend;
    }

    public void setRam_messageend(ram_MessageEnd ram_messageend) {
        this.ram_messageend = ram_messageend;
    }
    public List<ram_ParameterValueMapping> getRam_parametervaluemappings() {
        return ram_parametervaluemappings;
    }

    public void addRam_parametervaluemapping(Ram_parametervaluemapping ram_parametervaluemapping) {
        this.ram_parametervaluemappings.add(ram_parametervaluemapping);
    }
    public ram_MessageEnd getRam_messageend() {
        return ram_messageend;
    }

    public void setRam_messageend(ram_MessageEnd ram_messageend) {
        this.ram_messageend = ram_messageend;
    }
    public ram_Interaction getRam_interaction() {
        return ram_interaction;
    }

    public void setRam_interaction(ram_Interaction ram_interaction) {
        this.ram_interaction = ram_interaction;
    }

}