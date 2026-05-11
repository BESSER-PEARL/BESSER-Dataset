





import java.util.List;
import java.util.ArrayList;

public class iso20022_BroadcastList extends ModelEntity {






    private List<iso20022_Address> iso20022_addresss;




    private iso20022_Address iso20022_address;


    public iso20022_BroadcastList(
    ) {
        super(
        );
        this.iso20022_addresss = new ArrayList<>();
    }

    public iso20022_BroadcastList(
        ArrayList<iso20022_Address> iso20022_addresss    ) {
        this.iso20022_addresss = iso20022_addresss;
    }


    public List<iso20022_Address> getIso20022_addresss() {
        return iso20022_addresss;
    }

    public void addIso20022_address(Iso20022_address iso20022_address) {
        this.iso20022_addresss.add(iso20022_address);
    }
    public iso20022_Address getIso20022_address() {
        return iso20022_address;
    }

    public void setIso20022_address(iso20022_Address iso20022_address) {
        this.iso20022_address = iso20022_address;
    }

}