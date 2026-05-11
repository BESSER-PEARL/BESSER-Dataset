





import java.util.List;
import java.util.ArrayList;

public class ASD_Operation extends NamedElement {

    private String messagePattern;





    private ASD_ServiceDescription asd_servicedescription;




    private ASD_ServiceDescription asd_servicedescription;




    private List<ASD_Message> asd_messages;




    private ASD_Message asd_message;


    public ASD_Operation(
        String messagePattern    ) {
        super(
        );
        this.messagePattern = messagePattern;
        this.asd_messages = new ArrayList<>();
    }

    public ASD_Operation(
        String messagePattern        ArrayList<ASD_Message> asd_messages    ) {
        this.messagePattern = messagePattern;
        this.asd_messages = asd_messages;
    }

    public String getMessagepattern() {
        return messagePattern;
    }

    public void setMessagepattern(String messagePattern) {
        this.messagePattern = messagePattern;
    }

    public ASD_ServiceDescription getAsd_servicedescription() {
        return asd_servicedescription;
    }

    public void setAsd_servicedescription(ASD_ServiceDescription asd_servicedescription) {
        this.asd_servicedescription = asd_servicedescription;
    }
    public ASD_ServiceDescription getAsd_servicedescription() {
        return asd_servicedescription;
    }

    public void setAsd_servicedescription(ASD_ServiceDescription asd_servicedescription) {
        this.asd_servicedescription = asd_servicedescription;
    }
    public List<ASD_Message> getAsd_messages() {
        return asd_messages;
    }

    public void addAsd_message(Asd_message asd_message) {
        this.asd_messages.add(asd_message);
    }
    public ASD_Message getAsd_message() {
        return asd_message;
    }

    public void setAsd_message(ASD_Message asd_message) {
        this.asd_message = asd_message;
    }

}