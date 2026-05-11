





import java.util.List;
import java.util.ArrayList;

public class services_ServiceIncidentMgt  {

    private String businessImpact;
    private String maintenanceWindow;
    private String monitoring;
    private String maintenance;



    public services_ServiceIncidentMgt(
        String businessImpact,        String maintenanceWindow,        String monitoring,        String maintenance    ) {
        this.businessImpact = businessImpact;
        this.maintenanceWindow = maintenanceWindow;
        this.monitoring = monitoring;
        this.maintenance = maintenance;
    }


    public String getBusinessimpact() {
        return businessImpact;
    }

    public void setBusinessimpact(String businessImpact) {
        this.businessImpact = businessImpact;
    }
    public String getMaintenancewindow() {
        return maintenanceWindow;
    }

    public void setMaintenancewindow(String maintenanceWindow) {
        this.maintenanceWindow = maintenanceWindow;
    }
    public String getMonitoring() {
        return monitoring;
    }

    public void setMonitoring(String monitoring) {
        this.monitoring = monitoring;
    }
    public String getMaintenance() {
        return maintenance;
    }

    public void setMaintenance(String maintenance) {
        this.maintenance = maintenance;
    }


}