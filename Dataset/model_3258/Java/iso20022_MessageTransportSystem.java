





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageTransportSystem extends ModelEntity {






    private List<iso20022_MessagingEndpoint> iso20022_messagingendpoints;




    private iso20022_MessagingEndpoint iso20022_messagingendpoint;


    public iso20022_MessageTransportSystem(
    ) {
        super(
        );
        this.iso20022_messagingendpoints = new ArrayList<>();
    }

    public iso20022_MessageTransportSystem(
        ArrayList<iso20022_MessagingEndpoint> iso20022_messagingendpoints    ) {
        this.iso20022_messagingendpoints = iso20022_messagingendpoints;
    }


    public List<iso20022_MessagingEndpoint> getIso20022_messagingendpoints() {
        return iso20022_messagingendpoints;
    }

    public void addIso20022_messagingendpoint(Iso20022_messagingendpoint iso20022_messagingendpoint) {
        this.iso20022_messagingendpoints.add(iso20022_messagingendpoint);
    }
    public iso20022_MessagingEndpoint getIso20022_messagingendpoint() {
        return iso20022_messagingendpoint;
    }

    public void setIso20022_messagingendpoint(iso20022_MessagingEndpoint iso20022_messagingendpoint) {
        this.iso20022_messagingendpoint = iso20022_messagingendpoint;
    }

}