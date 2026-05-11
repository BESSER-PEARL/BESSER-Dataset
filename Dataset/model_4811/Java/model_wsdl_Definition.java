





import java.util.List;
import java.util.ArrayList;

public class model_wsdl_Definition extends wsdl_ExtensibleElement, wsdl_IDefinition {

    private String qName;
    private String encoding;
    private String location;
    private String targetNamespace;





    private List<PortType> porttypes;




    private List<Message> messages;


    public model_wsdl_Definition(
        String qName,        String encoding,        String location,        String targetNamespace    ) {
        super(
        );
        this.qName = qName;
        this.encoding = encoding;
        this.location = location;
        this.targetNamespace = targetNamespace;
        this.porttypes = new ArrayList<>();
        this.messages = new ArrayList<>();
    }

    public model_wsdl_Definition(
        String qName,        String encoding,        String location,        String targetNamespace        ArrayList<PortType> porttypes,        ArrayList<Message> messages    ) {
        this.qName = qName;
        this.encoding = encoding;
        this.location = location;
        this.targetNamespace = targetNamespace;
        this.porttypes = porttypes;
        this.messages = messages;
    }

    public String getQname() {
        return qName;
    }

    public void setQname(String qName) {
        this.qName = qName;
    }
    public String getEncoding() {
        return encoding;
    }

    public void setEncoding(String encoding) {
        this.encoding = encoding;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getTargetnamespace() {
        return targetNamespace;
    }

    public void setTargetnamespace(String targetNamespace) {
        this.targetNamespace = targetNamespace;
    }

    public List<PortType> getPorttypes() {
        return porttypes;
    }

    public void addPorttype(Porttype porttype) {
        this.porttypes.add(porttype);
    }
    public List<Message> getMessages() {
        return messages;
    }

    public void addMessage(Message message) {
        this.messages.add(message);
    }

}