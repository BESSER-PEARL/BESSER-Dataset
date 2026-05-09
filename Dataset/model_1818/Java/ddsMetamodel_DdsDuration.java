





import java.util.List;
import java.util.ArrayList;

public class ddsMetamodel_DdsDuration  {

    private String nanoSec;
    private String sec;





    private ddsMetamodel_DdsLatencyBudgetQos ddsmetamodel_ddslatencybudgetqos;




    private ddsMetamodel_DdsReliabilityQos ddsmetamodel_ddsreliabilityqos;




    private ddsMetamodel_DdsDeadlineQos ddsmetamodel_ddsdeadlineqos;




    private ddsMetamodel_DdsLivelinessQos ddsmetamodel_ddslivelinessqos;




    private ddsMetamodel_DdsDurabilityServiceQos ddsmetamodel_ddsdurabilityserviceqos;




    private ddsMetamodel_DdsLifespan ddsmetamodel_ddslifespan;


    public ddsMetamodel_DdsDuration(
        String nanoSec,        String sec    ) {
        this.nanoSec = nanoSec;
        this.sec = sec;
    }


    public String getNanosec() {
        return nanoSec;
    }

    public void setNanosec(String nanoSec) {
        this.nanoSec = nanoSec;
    }
    public String getSec() {
        return sec;
    }

    public void setSec(String sec) {
        this.sec = sec;
    }

    public ddsMetamodel_DdsLatencyBudgetQos getDdsmetamodel_ddslatencybudgetqos() {
        return ddsmetamodel_ddslatencybudgetqos;
    }

    public void setDdsmetamodel_ddslatencybudgetqos(ddsMetamodel_DdsLatencyBudgetQos ddsmetamodel_ddslatencybudgetqos) {
        this.ddsmetamodel_ddslatencybudgetqos = ddsmetamodel_ddslatencybudgetqos;
    }
    public ddsMetamodel_DdsReliabilityQos getDdsmetamodel_ddsreliabilityqos() {
        return ddsmetamodel_ddsreliabilityqos;
    }

    public void setDdsmetamodel_ddsreliabilityqos(ddsMetamodel_DdsReliabilityQos ddsmetamodel_ddsreliabilityqos) {
        this.ddsmetamodel_ddsreliabilityqos = ddsmetamodel_ddsreliabilityqos;
    }
    public ddsMetamodel_DdsDeadlineQos getDdsmetamodel_ddsdeadlineqos() {
        return ddsmetamodel_ddsdeadlineqos;
    }

    public void setDdsmetamodel_ddsdeadlineqos(ddsMetamodel_DdsDeadlineQos ddsmetamodel_ddsdeadlineqos) {
        this.ddsmetamodel_ddsdeadlineqos = ddsmetamodel_ddsdeadlineqos;
    }
    public ddsMetamodel_DdsLivelinessQos getDdsmetamodel_ddslivelinessqos() {
        return ddsmetamodel_ddslivelinessqos;
    }

    public void setDdsmetamodel_ddslivelinessqos(ddsMetamodel_DdsLivelinessQos ddsmetamodel_ddslivelinessqos) {
        this.ddsmetamodel_ddslivelinessqos = ddsmetamodel_ddslivelinessqos;
    }
    public ddsMetamodel_DdsDurabilityServiceQos getDdsmetamodel_ddsdurabilityserviceqos() {
        return ddsmetamodel_ddsdurabilityserviceqos;
    }

    public void setDdsmetamodel_ddsdurabilityserviceqos(ddsMetamodel_DdsDurabilityServiceQos ddsmetamodel_ddsdurabilityserviceqos) {
        this.ddsmetamodel_ddsdurabilityserviceqos = ddsmetamodel_ddsdurabilityserviceqos;
    }
    public ddsMetamodel_DdsLifespan getDdsmetamodel_ddslifespan() {
        return ddsmetamodel_ddslifespan;
    }

    public void setDdsmetamodel_ddslifespan(ddsMetamodel_DdsLifespan ddsmetamodel_ddslifespan) {
        this.ddsmetamodel_ddslifespan = ddsmetamodel_ddslifespan;
    }

}