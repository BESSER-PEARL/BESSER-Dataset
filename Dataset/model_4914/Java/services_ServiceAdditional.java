





import java.util.List;
import java.util.ArrayList;

public class services_ServiceAdditional  {

    private String lifeCycleState;
    private String report;
    private String costCenter;
    private String kpi;
    private String link;
    private String usageState;
    private String history;





    private services_Service services_service;


    public services_ServiceAdditional(
        String lifeCycleState,        String report,        String costCenter,        String kpi,        String link,        String usageState,        String history    ) {
        this.lifeCycleState = lifeCycleState;
        this.report = report;
        this.costCenter = costCenter;
        this.kpi = kpi;
        this.link = link;
        this.usageState = usageState;
        this.history = history;
    }


    public String getLifecyclestate() {
        return lifeCycleState;
    }

    public void setLifecyclestate(String lifeCycleState) {
        this.lifeCycleState = lifeCycleState;
    }
    public String getReport() {
        return report;
    }

    public void setReport(String report) {
        this.report = report;
    }
    public String getCostcenter() {
        return costCenter;
    }

    public void setCostcenter(String costCenter) {
        this.costCenter = costCenter;
    }
    public String getKpi() {
        return kpi;
    }

    public void setKpi(String kpi) {
        this.kpi = kpi;
    }
    public String getLink() {
        return link;
    }

    public void setLink(String link) {
        this.link = link;
    }
    public String getUsagestate() {
        return usageState;
    }

    public void setUsagestate(String usageState) {
        this.usageState = usageState;
    }
    public String getHistory() {
        return history;
    }

    public void setHistory(String history) {
        this.history = history;
    }

    public services_Service getServices_service() {
        return services_service;
    }

    public void setServices_service(services_Service services_service) {
        this.services_service = services_service;
    }

}