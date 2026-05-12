





import java.util.List;
import java.util.ArrayList;

public class driver_StartTrace  {

    private String disableSecondaryFilters;
    private String disablePrimaryFilters;
    private String enablePrimaryFilters;
    private String configFilePath;
    private String enableSecondaryFilters;





    private driver_Task driver_task;


    public driver_StartTrace(
        String disableSecondaryFilters,        String disablePrimaryFilters,        String enablePrimaryFilters,        String configFilePath,        String enableSecondaryFilters    ) {
        this.disableSecondaryFilters = disableSecondaryFilters;
        this.disablePrimaryFilters = disablePrimaryFilters;
        this.enablePrimaryFilters = enablePrimaryFilters;
        this.configFilePath = configFilePath;
        this.enableSecondaryFilters = enableSecondaryFilters;
    }


    public String getDisablesecondaryfilters() {
        return disableSecondaryFilters;
    }

    public void setDisablesecondaryfilters(String disableSecondaryFilters) {
        this.disableSecondaryFilters = disableSecondaryFilters;
    }
    public String getDisableprimaryfilters() {
        return disablePrimaryFilters;
    }

    public void setDisableprimaryfilters(String disablePrimaryFilters) {
        this.disablePrimaryFilters = disablePrimaryFilters;
    }
    public String getEnableprimaryfilters() {
        return enablePrimaryFilters;
    }

    public void setEnableprimaryfilters(String enablePrimaryFilters) {
        this.enablePrimaryFilters = enablePrimaryFilters;
    }
    public String getConfigfilepath() {
        return configFilePath;
    }

    public void setConfigfilepath(String configFilePath) {
        this.configFilePath = configFilePath;
    }
    public String getEnablesecondaryfilters() {
        return enableSecondaryFilters;
    }

    public void setEnablesecondaryfilters(String enableSecondaryFilters) {
        this.enableSecondaryFilters = enableSecondaryFilters;
    }

    public driver_Task getDriver_task() {
        return driver_task;
    }

    public void setDriver_task(driver_Task driver_task) {
        this.driver_task = driver_task;
    }

}