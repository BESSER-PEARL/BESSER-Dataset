





import java.util.List;
import java.util.ArrayList;

public class wsn_Objectives  {

    private String delay;
    private String lifetime;
    private String packetloss;
    private String memfootprint;



    public wsn_Objectives(
        String delay,        String lifetime,        String packetloss,        String memfootprint    ) {
        this.delay = delay;
        this.lifetime = lifetime;
        this.packetloss = packetloss;
        this.memfootprint = memfootprint;
    }


    public String getDelay() {
        return delay;
    }

    public void setDelay(String delay) {
        this.delay = delay;
    }
    public String getLifetime() {
        return lifetime;
    }

    public void setLifetime(String lifetime) {
        this.lifetime = lifetime;
    }
    public String getPacketloss() {
        return packetloss;
    }

    public void setPacketloss(String packetloss) {
        this.packetloss = packetloss;
    }
    public String getMemfootprint() {
        return memfootprint;
    }

    public void setMemfootprint(String memfootprint) {
        this.memfootprint = memfootprint;
    }


}