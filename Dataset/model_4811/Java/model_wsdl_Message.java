





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_Message extends wsdl_IMessage, wsdl_ExtensibleElement {

    private boolean undefined;
    private String qName;





    private List<Part> parts;


    public model_wsdl_Message(
        boolean undefined,        String qName    ) {
        super(
        );
        this.undefined = undefined;
        this.qName = qName;
        this.parts = new ArrayList<>();
    }

    public model_wsdl_Message(
        boolean undefined,        String qName        ArrayList<Part> parts    ) {
        this.undefined = undefined;
        this.qName = qName;
        this.parts = parts;
    }

    public boolean getUndefined() {
        return undefined;
    }

    public void setUndefined(boolean undefined) {
        this.undefined = undefined;
    }
    public String getQname() {
        return qName;
    }

    public void setQname(String qName) {
        this.qName = qName;
    }

    public List<Part> getParts() {
        return parts;
    }

    public void addPart(Part part) {
        this.parts.add(part);
    }

}