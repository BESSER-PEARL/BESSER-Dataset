





import java.util.List;
import java.util.ArrayList;

public class Model_Session  {

    private String track2;
    private String DeviceStatus;
    private int pan;



    public Model_Session(
        String track2,        String DeviceStatus,        int pan    ) {
        this.track2 = track2;
        this.DeviceStatus = DeviceStatus;
        this.pan = pan;
    }


    public String getTrack2() {
        return track2;
    }

    public void setTrack2(String track2) {
        this.track2 = track2;
    }
    public String getDevicestatus() {
        return DeviceStatus;
    }

    public void setDevicestatus(String DeviceStatus) {
        this.DeviceStatus = DeviceStatus;
    }
    public int getPan() {
        return pan;
    }

    public void setPan(int pan) {
        this.pan = pan;
    }


}