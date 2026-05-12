





import java.util.List;
import java.util.ArrayList;

public class Camera  {

    private int panAngle;
    private int zoomSetting;



    public Camera(
        int panAngle,        int zoomSetting    ) {
        this.panAngle = panAngle;
        this.zoomSetting = zoomSetting;
    }


    public int getPanangle() {
        return panAngle;
    }

    public void setPanangle(int panAngle) {
        this.panAngle = panAngle;
    }
    public int getZoomsetting() {
        return zoomSetting;
    }

    public void setZoomsetting(int zoomSetting) {
        this.zoomSetting = zoomSetting;
    }


}