





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_Image extends GraphicsAlgorithm {

    private String proportional;
    private String stretchH;
    private String stretchV;
    private String id;



    public mm_algorithms_Image(
        String proportional,        String stretchH,        String stretchV,        String id    ) {
        super(
        );
        this.proportional = proportional;
        this.stretchH = stretchH;
        this.stretchV = stretchV;
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


}