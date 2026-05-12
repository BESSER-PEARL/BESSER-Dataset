





import java.util.List;
import java.util.ArrayList;

public class MapService  {

    private float currentVersion;
    private String cimVersion;
    private String mapName;



    public MapService(
        float currentVersion,        String cimVersion,        String mapName    ) {
        this.currentVersion = currentVersion;
        this.cimVersion = cimVersion;
        this.mapName = mapName;
    }


    public float getCurrentversion() {
        return currentVersion;
    }

    public void setCurrentversion(float currentVersion) {
        this.currentVersion = currentVersion;
    }
    public String getCimversion() {
        return cimVersion;
    }

    public void setCimversion(String cimVersion) {
        this.cimVersion = cimVersion;
    }
    public String getMapname() {
        return mapName;
    }

    public void setMapname(String mapName) {
        this.mapName = mapName;
    }


}