





import java.util.List;
import java.util.ArrayList;

public class wsn_Runtime extends , PlatformElement {

    private String mote;
    private String environment;



    public wsn_Runtime(
        String mote,        String environment    ) {
        super(
        );
        this.mote = mote;
        this.environment = environment;
    }


    public String getMote() {
        return mote;
    }

    public void setMote(String mote) {
        this.mote = mote;
    }
    public String getEnvironment() {
        return environment;
    }

    public void setEnvironment(String environment) {
        this.environment = environment;
    }


}