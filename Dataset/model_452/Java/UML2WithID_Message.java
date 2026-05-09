





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_Message extends NamedElement {

    private String messageKind;
    private String messageSort;





    private UML2WithID_NamedElement uml2withid_namedelement;




    private List<UML2WithID_ValueSpecification> uml2withid_valuespecifications;




    private UML2WithID_Connector uml2withid_connector;


    public UML2WithID_Message(
        String messageKind,        String messageSort    ) {
        super(
        );
        this.messageKind = messageKind;
        this.messageSort = messageSort;
        this.uml2withid_valuespecifications = new ArrayList<>();
    }

    public UML2WithID_Message(
        String messageKind,        String messageSort        ArrayList<UML2WithID_ValueSpecification> uml2withid_valuespecifications    ) {
        this.messageKind = messageKind;
        this.messageSort = messageSort;
        this.uml2withid_valuespecifications = uml2withid_valuespecifications;
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

    public UML2WithID_NamedElement getUml2withid_namedelement() {
        return uml2withid_namedelement;
    }

    public void setUml2withid_namedelement(UML2WithID_NamedElement uml2withid_namedelement) {
        this.uml2withid_namedelement = uml2withid_namedelement;
    }
    public List<UML2WithID_ValueSpecification> getUml2withid_valuespecifications() {
        return uml2withid_valuespecifications;
    }

    public void addUml2withid_valuespecification(Uml2withid_valuespecification uml2withid_valuespecification) {
        this.uml2withid_valuespecifications.add(uml2withid_valuespecification);
    }
    public UML2WithID_Connector getUml2withid_connector() {
        return uml2withid_connector;
    }

    public void setUml2withid_connector(UML2WithID_Connector uml2withid_connector) {
        this.uml2withid_connector = uml2withid_connector;
    }

}