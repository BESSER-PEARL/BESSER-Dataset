





import java.util.List;
import java.util.ArrayList;

public class mm_styles_GradientColoredLocation  {

    private String locationValue;
    private String locationType;





    private styles_Color styles_color;


    public mm_styles_GradientColoredLocation(
        String locationValue,        String locationType    ) {
        this.locationValue = locationValue;
        this.locationType = locationType;
    }


    public String getLocationvalue() {
        return locationValue;
    }

    public void setLocationvalue(String locationValue) {
        this.locationValue = locationValue;
    }
    public String getLocationtype() {
        return locationType;
    }

    public void setLocationtype(String locationType) {
        this.locationType = locationType;
    }

    public styles_Color getStyles_color() {
        return styles_color;
    }

    public void setStyles_color(styles_Color styles_color) {
        this.styles_color = styles_color;
    }

}