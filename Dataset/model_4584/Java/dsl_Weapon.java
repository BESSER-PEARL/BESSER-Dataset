





import java.util.List;
import java.util.ArrayList;

public class dsl_Weapon  {

    private String sourceBone;
    private String range;
    private String name;
    private String directionBone;
    private int period;
    private String uIName;
    private int scanRange;





    private dsl_Model dsl_model;


    public dsl_Weapon(
        String sourceBone,        String range,        String name,        String directionBone,        int period,        String uIName,        int scanRange    ) {
        this.sourceBone = sourceBone;
        this.range = range;
        this.name = name;
        this.directionBone = directionBone;
        this.period = period;
        this.uIName = uIName;
        this.scanRange = scanRange;
    }


    public String getSourcebone() {
        return sourceBone;
    }

    public void setSourcebone(String sourceBone) {
        this.sourceBone = sourceBone;
    }
    public String getRange() {
        return range;
    }

    public void setRange(String range) {
        this.range = range;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDirectionbone() {
        return directionBone;
    }

    public void setDirectionbone(String directionBone) {
        this.directionBone = directionBone;
    }
    public int getPeriod() {
        return period;
    }

    public void setPeriod(int period) {
        this.period = period;
    }
    public String getUiname() {
        return uIName;
    }

    public void setUiname(String uIName) {
        this.uIName = uIName;
    }
    public int getScanrange() {
        return scanRange;
    }

    public void setScanrange(int scanRange) {
        this.scanRange = scanRange;
    }

    public dsl_Model getDsl_model() {
        return dsl_model;
    }

    public void setDsl_model(dsl_Model dsl_model) {
        this.dsl_model = dsl_model;
    }

}