





import java.util.List;
import java.util.ArrayList;

public class bpmn_SubProcess extends Graph, Activity {

    private String adhoc;
    private String isTransaction;



    public bpmn_SubProcess(
        String adhoc,        String isTransaction    ) {
        super(
        );
        this.adhoc = adhoc;
        this.isTransaction = isTransaction;
    }


    public String getAdhoc() {
        return adhoc;
    }

    public void setAdhoc(String adhoc) {
        this.adhoc = adhoc;
    }
    public String getIstransaction() {
        return isTransaction;
    }

    public void setIstransaction(String isTransaction) {
        this.isTransaction = isTransaction;
    }


}