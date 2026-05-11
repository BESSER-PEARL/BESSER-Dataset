





import java.util.List;
import java.util.ArrayList;

public class dg_Image extends GraphicalElement {

    private String isAspectRatioPreserved;
    private String source;





    private dg_Bounds dg_bounds;


    public dg_Image(
        String isAspectRatioPreserved,        String source    ) {
        super(
        );
        this.isAspectRatioPreserved = isAspectRatioPreserved;
        this.source = source;
    }


    public String getIsaspectratiopreserved() {
        return isAspectRatioPreserved;
    }

    public void setIsaspectratiopreserved(String isAspectRatioPreserved) {
        this.isAspectRatioPreserved = isAspectRatioPreserved;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }

    public dg_Bounds getDg_bounds() {
        return dg_bounds;
    }

    public void setDg_bounds(dg_Bounds dg_bounds) {
        this.dg_bounds = dg_bounds;
    }

}