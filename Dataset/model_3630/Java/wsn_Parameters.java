





import java.util.List;
import java.util.ArrayList;

public class wsn_Parameters  {

    private String macProtocol;
    private String netStack;
    private String routingProtocol;
    private String rdcProtocol;
    private String sleepScheduling;



    public wsn_Parameters(
        String macProtocol,        String netStack,        String routingProtocol,        String rdcProtocol,        String sleepScheduling    ) {
        this.macProtocol = macProtocol;
        this.netStack = netStack;
        this.routingProtocol = routingProtocol;
        this.rdcProtocol = rdcProtocol;
        this.sleepScheduling = sleepScheduling;
    }


    public String getMacprotocol() {
        return macProtocol;
    }

    public void setMacprotocol(String macProtocol) {
        this.macProtocol = macProtocol;
    }
    public String getNetstack() {
        return netStack;
    }

    public void setNetstack(String netStack) {
        this.netStack = netStack;
    }
    public String getRoutingprotocol() {
        return routingProtocol;
    }

    public void setRoutingprotocol(String routingProtocol) {
        this.routingProtocol = routingProtocol;
    }
    public String getRdcprotocol() {
        return rdcProtocol;
    }

    public void setRdcprotocol(String rdcProtocol) {
        this.rdcProtocol = rdcProtocol;
    }
    public String getSleepscheduling() {
        return sleepScheduling;
    }

    public void setSleepscheduling(String sleepScheduling) {
        this.sleepScheduling = sleepScheduling;
    }


}