





import java.util.List;
import java.util.ArrayList;

public class DatadiagramMLXForm_ColorEntry extends IXrequiredElt {

    private String rgb;





    private ColorsTable colorstable;


    public DatadiagramMLXForm_ColorEntry(
        String rgb    ) {
        super(
        );
        this.rgb = rgb;
    }


    public String getRgb() {
        return rgb;
    }

    public void setRgb(String rgb) {
        this.rgb = rgb;
    }

    public ColorsTable getColorstable() {
        return colorstable;
    }

    public void setColorstable(ColorsTable colorstable) {
        this.colorstable = colorstable;
    }

}