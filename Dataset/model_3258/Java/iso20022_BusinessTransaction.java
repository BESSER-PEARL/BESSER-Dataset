





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessTransaction extends TopLevelCatalogueEntry {






    private List<iso20022_BusinessTransaction> iso20022_businesstransactions;




    private iso20022_MessageTransportMode iso20022_messagetransportmode;




    private iso20022_BusinessTransaction iso20022_businesstransaction;




    private iso20022_MessageTransportMode iso20022_messagetransportmode;


    public iso20022_BusinessTransaction(
    ) {
        super(
        );
        this.iso20022_businesstransactions = new ArrayList<>();
    }

    public iso20022_BusinessTransaction(
        ArrayList<iso20022_BusinessTransaction> iso20022_businesstransactions    ) {
        this.iso20022_businesstransactions = iso20022_businesstransactions;
    }


    public List<iso20022_BusinessTransaction> getIso20022_businesstransactions() {
        return iso20022_businesstransactions;
    }

    public void addIso20022_businesstransaction(Iso20022_businesstransaction iso20022_businesstransaction) {
        this.iso20022_businesstransactions.add(iso20022_businesstransaction);
    }
    public iso20022_MessageTransportMode getIso20022_messagetransportmode() {
        return iso20022_messagetransportmode;
    }

    public void setIso20022_messagetransportmode(iso20022_MessageTransportMode iso20022_messagetransportmode) {
        this.iso20022_messagetransportmode = iso20022_messagetransportmode;
    }
    public iso20022_BusinessTransaction getIso20022_businesstransaction() {
        return iso20022_businesstransaction;
    }

    public void setIso20022_businesstransaction(iso20022_BusinessTransaction iso20022_businesstransaction) {
        this.iso20022_businesstransaction = iso20022_businesstransaction;
    }
    public iso20022_MessageTransportMode getIso20022_messagetransportmode() {
        return iso20022_messagetransportmode;
    }

    public void setIso20022_messagetransportmode(iso20022_MessageTransportMode iso20022_messagetransportmode) {
        this.iso20022_messagetransportmode = iso20022_messagetransportmode;
    }

}