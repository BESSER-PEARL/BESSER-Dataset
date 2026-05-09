





import java.util.List;
import java.util.ArrayList;

public class appBuilderDSL_Main  {

    private String devices;
    private String appVersion;
    private String generalStyle;
    private String appName;





    private appBuilderDSL_Ui appbuilderdsl_ui;


    public appBuilderDSL_Main(
        String devices,        String appVersion,        String generalStyle,        String appName    ) {
        this.devices = devices;
        this.appVersion = appVersion;
        this.generalStyle = generalStyle;
        this.appName = appName;
    }


    public String getDevices() {
        return devices;
    }

    public void setDevices(String devices) {
        this.devices = devices;
    }
    public String getAppversion() {
        return appVersion;
    }

    public void setAppversion(String appVersion) {
        this.appVersion = appVersion;
    }
    public String getGeneralstyle() {
        return generalStyle;
    }

    public void setGeneralstyle(String generalStyle) {
        this.generalStyle = generalStyle;
    }
    public String getAppname() {
        return appName;
    }

    public void setAppname(String appName) {
        this.appName = appName;
    }

    public appBuilderDSL_Ui getAppbuilderdsl_ui() {
        return appbuilderdsl_ui;
    }

    public void setAppbuilderdsl_ui(appBuilderDSL_Ui appbuilderdsl_ui) {
        this.appbuilderdsl_ui = appbuilderdsl_ui;
    }

}