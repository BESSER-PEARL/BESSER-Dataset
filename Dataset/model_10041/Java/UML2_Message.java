





import java.util.List;
import java.util.ArrayList;

public class UML2_Message extends NamedElement {

    private String messageKind;
    private String messageSort;





    private UML2_MessageEnd uml2_messageend;




    private UML2_MessageEnd uml2_messageend;




    private List<UML2_ValueSpecification> uml2_valuespecifications;




    private UML2_NamedElement uml2_namedelement;




    private UML2_MessageEnd uml2_messageend;




    private UML2_MessageEnd uml2_messageend;


    public UML2_Message(
        String messageKind,        String messageSort    ) {
        super(
        );
        this.messageKind = messageKind;
        this.messageSort = messageSort;
        this.uml2_valuespecifications = new ArrayList<>();
    }

    public UML2_Message(
        String messageKind,        String messageSort        ArrayList<UML2_ValueSpecification> uml2_valuespecifications    ) {
        this.messageKind = messageKind;
        this.messageSort = messageSort;
        this.uml2_valuespecifications = uml2_valuespecifications;
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

    public UML2_MessageEnd getUml2_messageend() {
        return uml2_messageend;
    }

    public void setUml2_messageend(UML2_MessageEnd uml2_messageend) {
        this.uml2_messageend = uml2_messageend;
    }
    public UML2_MessageEnd getUml2_messageend() {
        return uml2_messageend;
    }

    public void setUml2_messageend(UML2_MessageEnd uml2_messageend) {
        this.uml2_messageend = uml2_messageend;
    }
    public List<UML2_ValueSpecification> getUml2_valuespecifications() {
        return uml2_valuespecifications;
    }

    public void addUml2_valuespecification(Uml2_valuespecification uml2_valuespecification) {
        this.uml2_valuespecifications.add(uml2_valuespecification);
    }
    public UML2_NamedElement getUml2_namedelement() {
        return uml2_namedelement;
    }

    public void setUml2_namedelement(UML2_NamedElement uml2_namedelement) {
        this.uml2_namedelement = uml2_namedelement;
    }
    public UML2_MessageEnd getUml2_messageend() {
        return uml2_messageend;
    }

    public void setUml2_messageend(UML2_MessageEnd uml2_messageend) {
        this.uml2_messageend = uml2_messageend;
    }
    public UML2_MessageEnd getUml2_messageend() {
        return uml2_messageend;
    }

    public void setUml2_messageend(UML2_MessageEnd uml2_messageend) {
        this.uml2_messageend = uml2_messageend;
    }

}