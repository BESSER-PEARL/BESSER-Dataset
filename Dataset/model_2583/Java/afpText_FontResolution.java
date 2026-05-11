





import java.util.List;
import java.util.ArrayList;

public class afpText_FontResolution extends triplet {

    private String RPuBase;
    private String RPUnits;
    private String MetTech;



    public afpText_FontResolution(
        String RPuBase,        String RPUnits,        String MetTech    ) {
        super(
        );
        this.RPuBase = RPuBase;
        this.RPUnits = RPUnits;
        this.MetTech = MetTech;
    }


    public String getRpubase() {
        return RPuBase;
    }

    public void setRpubase(String RPuBase) {
        this.RPuBase = RPuBase;
    }
    public String getRpunits() {
        return RPUnits;
    }

    public void setRpunits(String RPUnits) {
        this.RPUnits = RPUnits;
    }
    public String getMettech() {
        return MetTech;
    }

    public void setMettech(String MetTech) {
        this.MetTech = MetTech;
    }


}