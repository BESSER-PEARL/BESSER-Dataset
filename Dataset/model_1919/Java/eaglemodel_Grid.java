





import java.util.List;
import java.util.ArrayList;

public class eaglemodel_Grid  {

    private int multiple;
    private boolean display;
    private String altunit;
    private String unitdist;
    private String altunitdist;
    private String unit;
    private float altdistance;
    private float distance;
    private String style;



    public eaglemodel_Grid(
        int multiple,        boolean display,        String altunit,        String unitdist,        String altunitdist,        String unit,        float altdistance,        float distance,        String style    ) {
        this.multiple = multiple;
        this.display = display;
        this.altunit = altunit;
        this.unitdist = unitdist;
        this.altunitdist = altunitdist;
        this.unit = unit;
        this.altdistance = altdistance;
        this.distance = distance;
        this.style = style;
    }


    public int getMultiple() {
        return multiple;
    }

    public void setMultiple(int multiple) {
        this.multiple = multiple;
    }
    public boolean getDisplay() {
        return display;
    }

    public void setDisplay(boolean display) {
        this.display = display;
    }
    public String getAltunit() {
        return altunit;
    }

    public void setAltunit(String altunit) {
        this.altunit = altunit;
    }
    public String getUnitdist() {
        return unitdist;
    }

    public void setUnitdist(String unitdist) {
        this.unitdist = unitdist;
    }
    public String getAltunitdist() {
        return altunitdist;
    }

    public void setAltunitdist(String altunitdist) {
        this.altunitdist = altunitdist;
    }
    public String getUnit() {
        return unit;
    }

    public void setUnit(String unit) {
        this.unit = unit;
    }
    public float getAltdistance() {
        return altdistance;
    }

    public void setAltdistance(float altdistance) {
        this.altdistance = altdistance;
    }
    public float getDistance() {
        return distance;
    }

    public void setDistance(float distance) {
        this.distance = distance;
    }
    public String getStyle() {
        return style;
    }

    public void setStyle(String style) {
        this.style = style;
    }


}