





import java.util.List;
import java.util.ArrayList;

public class nupn_StructureType  {

    private String units;
    private String safe;
    private String root;



    public nupn_StructureType(
        String units,        String safe,        String root    ) {
        this.units = units;
        this.safe = safe;
        this.root = root;
    }


    public String getUnits() {
        return units;
    }

    public void setUnits(String units) {
        this.units = units;
    }
    public String getSafe() {
        return safe;
    }

    public void setSafe(String safe) {
        this.safe = safe;
    }
    public String getRoot() {
        return root;
    }

    public void setRoot(String root) {
        this.root = root;
    }


}