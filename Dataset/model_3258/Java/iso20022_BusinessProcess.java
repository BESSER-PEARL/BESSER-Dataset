





import java.util.List;
import java.util.ArrayList;

public class iso20022_BusinessProcess extends TopLevelCatalogueEntry {






    private List<iso20022_BusinessTransaction> iso20022_businesstransactions;




    private List<iso20022_BusinessProcess> iso20022_businessprocesss;




    private iso20022_BusinessProcess iso20022_businessprocess;




    private iso20022_BusinessProcess iso20022_businessprocess;




    private iso20022_BusinessTransaction iso20022_businesstransaction;




    private iso20022_BusinessProcess iso20022_businessprocess;


    public iso20022_BusinessProcess(
    ) {
        super(
        );
        this.iso20022_businesstransactions = new ArrayList<>();
        this.iso20022_businessprocesss = new ArrayList<>();
    }

    public iso20022_BusinessProcess(
        ArrayList<iso20022_BusinessTransaction> iso20022_businesstransactions,        ArrayList<iso20022_BusinessProcess> iso20022_businessprocesss    ) {
        this.iso20022_businesstransactions = iso20022_businesstransactions;
        this.iso20022_businessprocesss = iso20022_businessprocesss;
    }


    public List<iso20022_BusinessTransaction> getIso20022_businesstransactions() {
        return iso20022_businesstransactions;
    }

    public void addIso20022_businesstransaction(Iso20022_businesstransaction iso20022_businesstransaction) {
        this.iso20022_businesstransactions.add(iso20022_businesstransaction);
    }
    public List<iso20022_BusinessProcess> getIso20022_businessprocesss() {
        return iso20022_businessprocesss;
    }

    public void addIso20022_businessprocess(Iso20022_businessprocess iso20022_businessprocess) {
        this.iso20022_businessprocesss.add(iso20022_businessprocess);
    }
    public iso20022_BusinessProcess getIso20022_businessprocess() {
        return iso20022_businessprocess;
    }

    public void setIso20022_businessprocess(iso20022_BusinessProcess iso20022_businessprocess) {
        this.iso20022_businessprocess = iso20022_businessprocess;
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
    public iso20022_BusinessProcess getIso20022_businessprocess() {
        return iso20022_businessprocess;
    }

    public void setIso20022_businessprocess(iso20022_BusinessProcess iso20022_businessprocess) {
        this.iso20022_businessprocess = iso20022_businessprocess;
    }

}