





import java.util.List;
import java.util.ArrayList;

public class sipme_BusinessProcess extends EnterpriseProcessor {

    private int ProcessPriority;





    private List<sipme_Activity> sipme_activitys;




    private sipme_Activity sipme_activity;




    private sipme_Domain sipme_domain;




    private sipme_Domain sipme_domain;


    public sipme_BusinessProcess(
        int ProcessPriority    ) {
        super(
        );
        this.ProcessPriority = ProcessPriority;
        this.sipme_activitys = new ArrayList<>();
    }

    public sipme_BusinessProcess(
        int ProcessPriority        ArrayList<sipme_Activity> sipme_activitys    ) {
        this.ProcessPriority = ProcessPriority;
        this.sipme_activitys = sipme_activitys;
    }

    public int getProcesspriority() {
        return ProcessPriority;
    }

    public void setProcesspriority(int ProcessPriority) {
        this.ProcessPriority = ProcessPriority;
    }

    public List<sipme_Activity> getSipme_activitys() {
        return sipme_activitys;
    }

    public void addSipme_activity(Sipme_activity sipme_activity) {
        this.sipme_activitys.add(sipme_activity);
    }
    public sipme_Activity getSipme_activity() {
        return sipme_activity;
    }

    public void setSipme_activity(sipme_Activity sipme_activity) {
        this.sipme_activity = sipme_activity;
    }
    public sipme_Domain getSipme_domain() {
        return sipme_domain;
    }

    public void setSipme_domain(sipme_Domain sipme_domain) {
        this.sipme_domain = sipme_domain;
    }
    public sipme_Domain getSipme_domain() {
        return sipme_domain;
    }

    public void setSipme_domain(sipme_Domain sipme_domain) {
        this.sipme_domain = sipme_domain;
    }

}