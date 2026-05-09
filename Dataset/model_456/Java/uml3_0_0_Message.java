





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_Message extends NamedElement {

    private String messageKind;
    private String messageSort;





    private uml3_0_0_MessageEnd uml3_0_0_messageend;




    private List<uml3_0_0_ValueSpecification> uml3_0_0_valuespecifications;




    private uml3_0_0_InformationFlow uml3_0_0_informationflow;




    private uml3_0_0_MessageEnd uml3_0_0_messageend;




    private uml3_0_0_MessageEnd uml3_0_0_messageend;




    private uml3_0_0_NamedElement uml3_0_0_namedelement;


    public uml3_0_0_Message(
        String messageKind,        String messageSort    ) {
        super(
        );
        this.messageKind = messageKind;
        this.messageSort = messageSort;
        this.uml3_0_0_valuespecifications = new ArrayList<>();
    }

    public uml3_0_0_Message(
        String messageKind,        String messageSort        ArrayList<uml3_0_0_ValueSpecification> uml3_0_0_valuespecifications    ) {
        this.messageKind = messageKind;
        this.messageSort = messageSort;
        this.uml3_0_0_valuespecifications = uml3_0_0_valuespecifications;
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

    public uml3_0_0_MessageEnd getUml3_0_0_messageend() {
        return uml3_0_0_messageend;
    }

    public void setUml3_0_0_messageend(uml3_0_0_MessageEnd uml3_0_0_messageend) {
        this.uml3_0_0_messageend = uml3_0_0_messageend;
    }
    public List<uml3_0_0_ValueSpecification> getUml3_0_0_valuespecifications() {
        return uml3_0_0_valuespecifications;
    }

    public void addUml3_0_0_valuespecification(Uml3_0_0_valuespecification uml3_0_0_valuespecification) {
        this.uml3_0_0_valuespecifications.add(uml3_0_0_valuespecification);
    }
    public uml3_0_0_InformationFlow getUml3_0_0_informationflow() {
        return uml3_0_0_informationflow;
    }

    public void setUml3_0_0_informationflow(uml3_0_0_InformationFlow uml3_0_0_informationflow) {
        this.uml3_0_0_informationflow = uml3_0_0_informationflow;
    }
    public uml3_0_0_MessageEnd getUml3_0_0_messageend() {
        return uml3_0_0_messageend;
    }

    public void setUml3_0_0_messageend(uml3_0_0_MessageEnd uml3_0_0_messageend) {
        this.uml3_0_0_messageend = uml3_0_0_messageend;
    }
    public uml3_0_0_MessageEnd getUml3_0_0_messageend() {
        return uml3_0_0_messageend;
    }

    public void setUml3_0_0_messageend(uml3_0_0_MessageEnd uml3_0_0_messageend) {
        this.uml3_0_0_messageend = uml3_0_0_messageend;
    }
    public uml3_0_0_NamedElement getUml3_0_0_namedelement() {
        return uml3_0_0_namedelement;
    }

    public void setUml3_0_0_namedelement(uml3_0_0_NamedElement uml3_0_0_namedelement) {
        this.uml3_0_0_namedelement = uml3_0_0_namedelement;
    }

}