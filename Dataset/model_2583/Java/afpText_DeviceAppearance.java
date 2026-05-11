





import java.util.List;
import java.util.ArrayList;

public class afpText_DeviceAppearance extends triplet {

    private String DevApp;
    private String Reserved;



    public afpText_DeviceAppearance(
        String DevApp,        String Reserved    ) {
        super(
        );
        this.DevApp = DevApp;
        this.Reserved = Reserved;
    }


    public String getDevapp() {
        return DevApp;
    }

    public void setDevapp(String DevApp) {
        this.DevApp = DevApp;
    }
    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }


}