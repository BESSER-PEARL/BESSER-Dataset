





import java.util.List;
import java.util.ArrayList;

public class dg_Image extends GraphicalElement {

    private String source;
    private String isAspectRatioPreserved;





    private dg_Bounds dg_bounds;


    public dg_Image(
        String source,        String isAspectRatioPreserved    ) {
        super(
        );
        this.source = source;
        this.isAspectRatioPreserved = isAspectRatioPreserved;
    }


    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getIsaspectratiopreserved() {
        return isAspectRatioPreserved;
    }

    public void setIsaspectratiopreserved(String isAspectRatioPreserved) {
        this.isAspectRatioPreserved = isAspectRatioPreserved;
    }

    public dg_Bounds getDg_bounds() {
        return dg_bounds;
    }

    public void setDg_bounds(dg_Bounds dg_bounds) {
        this.dg_bounds = dg_bounds;
    }

}