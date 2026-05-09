





import java.util.List;
import java.util.ArrayList;

public class uml_Message extends NamedElement {

    private String messageSort;
    private String messageKind;





    private uml_MessageEnd uml_messageend;




    private uml_NamedElement uml_namedelement;




    private uml_InformationFlow uml_informationflow;




    private uml_MessageEnd uml_messageend;




    private List<uml_ValueSpecification> uml_valuespecifications;




    private uml_MessageEnd uml_messageend;


    public uml_Message(
        String messageSort,        String messageKind    ) {
        super(
        );
        this.messageSort = messageSort;
        this.messageKind = messageKind;
        this.uml_valuespecifications = new ArrayList<>();
    }

    public uml_Message(
        String messageSort,        String messageKind        ArrayList<uml_ValueSpecification> uml_valuespecifications    ) {
        this.messageSort = messageSort;
        this.messageKind = messageKind;
        this.uml_valuespecifications = uml_valuespecifications;
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

    public uml_MessageEnd getUml_messageend() {
        return uml_messageend;
    }

    public void setUml_messageend(uml_MessageEnd uml_messageend) {
        this.uml_messageend = uml_messageend;
    }
    public uml_NamedElement getUml_namedelement() {
        return uml_namedelement;
    }

    public void setUml_namedelement(uml_NamedElement uml_namedelement) {
        this.uml_namedelement = uml_namedelement;
    }
    public uml_InformationFlow getUml_informationflow() {
        return uml_informationflow;
    }

    public void setUml_informationflow(uml_InformationFlow uml_informationflow) {
        this.uml_informationflow = uml_informationflow;
    }
    public uml_MessageEnd getUml_messageend() {
        return uml_messageend;
    }

    public void setUml_messageend(uml_MessageEnd uml_messageend) {
        this.uml_messageend = uml_messageend;
    }
    public List<uml_ValueSpecification> getUml_valuespecifications() {
        return uml_valuespecifications;
    }

    public void addUml_valuespecification(Uml_valuespecification uml_valuespecification) {
        this.uml_valuespecifications.add(uml_valuespecification);
    }
    public uml_MessageEnd getUml_messageend() {
        return uml_messageend;
    }

    public void setUml_messageend(uml_MessageEnd uml_messageend) {
        this.uml_messageend = uml_messageend;
    }

}