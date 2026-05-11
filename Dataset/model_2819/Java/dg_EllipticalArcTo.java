





import java.util.List;
import java.util.ArrayList;

public class dg_EllipticalArcTo extends PathCommand {

    private String rotation;
    private String isLargeArc;
    private String isSweep;



    public dg_EllipticalArcTo(
        String rotation,        String isLargeArc,        String isSweep    ) {
        super(
        );
        this.rotation = rotation;
        this.isLargeArc = isLargeArc;
        this.isSweep = isSweep;
    }


    public String getRotation() {
        return rotation;
    }

    public void setRotation(String rotation) {
        this.rotation = rotation;
    }
    public String getIslargearc() {
        return isLargeArc;
    }

    public void setIslargearc(String isLargeArc) {
        this.isLargeArc = isLargeArc;
    }
    public String getIssweep() {
        return isSweep;
    }

    public void setIssweep(String isSweep) {
        this.isSweep = isSweep;
    }


}