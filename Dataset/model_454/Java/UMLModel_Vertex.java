





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Vertex extends NamedElement {

    private String outgoing;
    private String container;
    private String incoming;



    public UMLModel_Vertex(
        String outgoing,        String container,        String incoming    ) {
        super(
        );
        this.outgoing = outgoing;
        this.container = container;
        this.incoming = incoming;
    }


    public String getOutgoing() {
        return outgoing;
    }

    public void setOutgoing(String outgoing) {
        this.outgoing = outgoing;
    }
    public String getContainer() {
        return container;
    }

    public void setContainer(String container) {
        this.container = container;
    }
    public String getIncoming() {
        return incoming;
    }

    public void setIncoming(String incoming) {
        this.incoming = incoming;
    }


}