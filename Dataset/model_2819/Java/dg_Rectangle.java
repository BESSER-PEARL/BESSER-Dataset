





import java.util.List;
import java.util.ArrayList;

public class dg_Rectangle extends GraphicalElement {

    private String cornerRadius;





    private dg_Bounds dg_bounds;


    public dg_Rectangle(
        String cornerRadius    ) {
        super(
        );
        this.cornerRadius = cornerRadius;
    }


    public String getCornerradius() {
        return cornerRadius;
    }

    public void setCornerradius(String cornerRadius) {
        this.cornerRadius = cornerRadius;
    }

    public dg_Bounds getDg_bounds() {
        return dg_bounds;
    }

    public void setDg_bounds(dg_Bounds dg_bounds) {
        this.dg_bounds = dg_bounds;
    }

}