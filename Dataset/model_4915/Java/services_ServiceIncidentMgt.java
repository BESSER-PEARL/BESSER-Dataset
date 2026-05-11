





import java.util.List;
import java.util.ArrayList;

public class services_ServiceIncidentMgt  {

    private String maintenance;
    private String monitoring;
    private String maintenanceWindow;
    private String businessImpact;



    public services_ServiceIncidentMgt(
        String maintenance,        String monitoring,        String maintenanceWindow,        String businessImpact    ) {
        this.maintenance = maintenance;
        this.monitoring = monitoring;
        this.maintenanceWindow = maintenanceWindow;
        this.businessImpact = businessImpact;
    }


    public String getMaintenance() {
        return maintenance;
    }

    public void setMaintenance(String maintenance) {
        this.maintenance = maintenance;
    }
    public String getMonitoring() {
        return monitoring;
    }

    public void setMonitoring(String monitoring) {
        this.monitoring = monitoring;
    }
    public String getMaintenancewindow() {
        return maintenanceWindow;
    }

    public void setMaintenancewindow(String maintenanceWindow) {
        this.maintenanceWindow = maintenanceWindow;
    }
    public String getBusinessimpact() {
        return businessImpact;
    }

    public void setBusinessimpact(String businessImpact) {
        this.businessImpact = businessImpact;
    }


}