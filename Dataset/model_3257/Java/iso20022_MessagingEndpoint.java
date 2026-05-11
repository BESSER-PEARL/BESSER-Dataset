





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessagingEndpoint extends ModelEntity {






    private iso20022_MessageTransportSystem iso20022_messagetransportsystem;




    private iso20022_Address iso20022_address;




    private List<iso20022_Address> iso20022_addresss;




    private iso20022_MessageTransportSystem iso20022_messagetransportsystem;


    public iso20022_MessagingEndpoint(
    ) {
        super(
        );
        this.iso20022_addresss = new ArrayList<>();
    }

    public iso20022_MessagingEndpoint(
        ArrayList<iso20022_Address> iso20022_addresss    ) {
        this.iso20022_addresss = iso20022_addresss;
    }


    public iso20022_MessageTransportSystem getIso20022_messagetransportsystem() {
        return iso20022_messagetransportsystem;
    }

    public void setIso20022_messagetransportsystem(iso20022_MessageTransportSystem iso20022_messagetransportsystem) {
        this.iso20022_messagetransportsystem = iso20022_messagetransportsystem;
    }
    public iso20022_Address getIso20022_address() {
        return iso20022_address;
    }

    public void setIso20022_address(iso20022_Address iso20022_address) {
        this.iso20022_address = iso20022_address;
    }
    public List<iso20022_Address> getIso20022_addresss() {
        return iso20022_addresss;
    }

    public void addIso20022_address(Iso20022_address iso20022_address) {
        this.iso20022_addresss.add(iso20022_address);
    }
    public iso20022_MessageTransportSystem getIso20022_messagetransportsystem() {
        return iso20022_messagetransportsystem;
    }

    public void setIso20022_messagetransportsystem(iso20022_MessageTransportSystem iso20022_messagetransportsystem) {
        this.iso20022_messagetransportsystem = iso20022_messagetransportsystem;
    }

}