





import java.util.List;
import java.util.ArrayList;

public class Fan  {

    private String FanID;





    private Light light;


    public Fan(
        String FanID    ) {
        this.FanID = FanID;
    }


    public String getFanid() {
        return FanID;
    }

    public void setFanid(String FanID) {
        this.FanID = FanID;
    }

    public Light getLight() {
        return light;
    }

    public void setLight(Light light) {
        this.light = light;
    }

}