





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_Image extends GraphicsAlgorithm {

    private String stretchV;
    private String id;
    private String proportional;
    private String stretchH;



    public mm_algorithms_Image(
        String stretchV,        String id,        String proportional,        String stretchH    ) {
        super(
        );
        this.stretchV = stretchV;
        this.id = id;
        this.proportional = proportional;
        this.stretchH = stretchH;
    }


    public String getStretchv() {
        return stretchV;
    }

    public void setStretchv(String stretchV) {
        this.stretchV = stretchV;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getProportional() {
        return proportional;
    }

    public void setProportional(String proportional) {
        this.proportional = proportional;
    }
    public String getStretchh() {
        return stretchH;
    }

    public void setStretchh(String stretchH) {
        this.stretchH = stretchH;
    }


}