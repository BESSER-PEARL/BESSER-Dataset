





import java.util.List;
import java.util.ArrayList;

public class model_values_Cylinder extends VisualValue {

    private String topRadius;
    private String bottomRadius;
    private String height;



    public model_values_Cylinder(
        String topRadius,        String bottomRadius,        String height    ) {
        super(
        );
        this.topRadius = topRadius;
        this.bottomRadius = bottomRadius;
        this.height = height;
    }


    public String getTopradius() {
        return topRadius;
    }

    public void setTopradius(String topRadius) {
        this.topRadius = topRadius;
    }
    public String getBottomradius() {
        return bottomRadius;
    }

    public void setBottomradius(String bottomRadius) {
        this.bottomRadius = bottomRadius;
    }
    public String getHeight() {
        return height;
    }

    public void setHeight(String height) {
        this.height = height;
    }


}