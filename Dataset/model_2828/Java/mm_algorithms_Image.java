





import java.util.List;
import java.util.ArrayList;

public class mm_algorithms_Image extends GraphicsAlgorithm {

    private String stretchH;
    private String id;
    private String proportional;
    private String stretchV;



    public mm_algorithms_Image(
        String stretchH,        String id,        String proportional,        String stretchV    ) {
        super(
        );
        this.stretchH = stretchH;
        this.id = id;
        this.proportional = proportional;
        this.stretchV = stretchV;
    }


    public String getStretchh() {
        return stretchH;
    }

    public void setStretchh(String stretchH) {
        this.stretchH = stretchH;
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
    public String getStretchv() {
        return stretchV;
    }

    public void setStretchv(String stretchV) {
        this.stretchV = stretchV;
    }


}