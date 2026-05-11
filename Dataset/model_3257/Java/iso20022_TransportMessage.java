





import java.util.List;
import java.util.ArrayList;

public class iso20022_TransportMessage extends ModelEntity {






    private iso20022_MessagingEndpoint iso20022_messagingendpoint;




    private iso20022_MessageInstance iso20022_messageinstance;




    private iso20022_MessagingEndpoint iso20022_messagingendpoint;




    private iso20022_MessagingEndpoint iso20022_messagingendpoint;




    private List<iso20022_MessagingEndpoint> iso20022_messagingendpoints;




    private iso20022_MessageInstance iso20022_messageinstance;


    public iso20022_TransportMessage(
    ) {
        super(
        );
        this.iso20022_messagingendpoints = new ArrayList<>();
    }

    public iso20022_TransportMessage(
        ArrayList<iso20022_MessagingEndpoint> iso20022_messagingendpoints    ) {
        this.iso20022_messagingendpoints = iso20022_messagingendpoints;
    }


    public iso20022_MessagingEndpoint getIso20022_messagingendpoint() {
        return iso20022_messagingendpoint;
    }

    public void setIso20022_messagingendpoint(iso20022_MessagingEndpoint iso20022_messagingendpoint) {
        this.iso20022_messagingendpoint = iso20022_messagingendpoint;
    }
    public iso20022_MessageInstance getIso20022_messageinstance() {
        return iso20022_messageinstance;
    }

    public void setIso20022_messageinstance(iso20022_MessageInstance iso20022_messageinstance) {
        this.iso20022_messageinstance = iso20022_messageinstance;
    }
    public iso20022_MessagingEndpoint getIso20022_messagingendpoint() {
        return iso20022_messagingendpoint;
    }

    public void setIso20022_messagingendpoint(iso20022_MessagingEndpoint iso20022_messagingendpoint) {
        this.iso20022_messagingendpoint = iso20022_messagingendpoint;
    }
    public iso20022_MessagingEndpoint getIso20022_messagingendpoint() {
        return iso20022_messagingendpoint;
    }

    public void setIso20022_messagingendpoint(iso20022_MessagingEndpoint iso20022_messagingendpoint) {
        this.iso20022_messagingendpoint = iso20022_messagingendpoint;
    }
    public List<iso20022_MessagingEndpoint> getIso20022_messagingendpoints() {
        return iso20022_messagingendpoints;
    }

    public void addIso20022_messagingendpoint(Iso20022_messagingendpoint iso20022_messagingendpoint) {
        this.iso20022_messagingendpoints.add(iso20022_messagingendpoint);
    }
    public iso20022_MessageInstance getIso20022_messageinstance() {
        return iso20022_messageinstance;
    }

    public void setIso20022_messageinstance(iso20022_MessageInstance iso20022_messageinstance) {
        this.iso20022_messageinstance = iso20022_messageinstance;
    }

}