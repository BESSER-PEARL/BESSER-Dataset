





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessTransaction extends TopLevelCatalogueEntry {






    private iso20022_BusinessProcess iso20022_businessprocess;




    private iso20022_BusinessTransaction iso20022_businesstransaction;




    private iso20022_BusinessTransaction iso20022_businesstransaction;




    private iso20022_MessageTransportMode iso20022_messagetransportmode;




    private iso20022_MessageTransportMode iso20022_messagetransportmode;




    private List<iso20022_MessageChoreography> iso20022_messagechoreographys;




    private iso20022_BusinessProcess iso20022_businessprocess;




    private iso20022_MessageChoreography iso20022_messagechoreography;


    public iso20022_BusinessTransaction(
    ) {
        super(
        );
        this.iso20022_messagechoreographys = new ArrayList<>();
    }

    public iso20022_BusinessTransaction(
        ArrayList<iso20022_MessageChoreography> iso20022_messagechoreographys    ) {
        this.iso20022_messagechoreographys = iso20022_messagechoreographys;
    }


    public iso20022_BusinessProcess getIso20022_businessprocess() {
        return iso20022_businessprocess;
    }

    public void setIso20022_businessprocess(iso20022_BusinessProcess iso20022_businessprocess) {
        this.iso20022_businessprocess = iso20022_businessprocess;
    }
    public iso20022_BusinessTransaction getIso20022_businesstransaction() {
        return iso20022_businesstransaction;
    }

    public void setIso20022_businesstransaction(iso20022_BusinessTransaction iso20022_businesstransaction) {
        this.iso20022_businesstransaction = iso20022_businesstransaction;
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
    public iso20022_MessageTransportMode getIso20022_messagetransportmode() {
        return iso20022_messagetransportmode;
    }

    public void setIso20022_messagetransportmode(iso20022_MessageTransportMode iso20022_messagetransportmode) {
        this.iso20022_messagetransportmode = iso20022_messagetransportmode;
    }
    public List<iso20022_MessageChoreography> getIso20022_messagechoreographys() {
        return iso20022_messagechoreographys;
    }

    public void addIso20022_messagechoreography(Iso20022_messagechoreography iso20022_messagechoreography) {
        this.iso20022_messagechoreographys.add(iso20022_messagechoreography);
    }
    public iso20022_BusinessProcess getIso20022_businessprocess() {
        return iso20022_businessprocess;
    }

    public void setIso20022_businessprocess(iso20022_BusinessProcess iso20022_businessprocess) {
        this.iso20022_businessprocess = iso20022_businessprocess;
    }
    public iso20022_MessageChoreography getIso20022_messagechoreography() {
        return iso20022_messagechoreography;
    }

    public void setIso20022_messagechoreography(iso20022_MessageChoreography iso20022_messagechoreography) {
        this.iso20022_messagechoreography = iso20022_messagechoreography;
    }

}