





import java.util.List;
import java.util.ArrayList;

public class mm_styles_GradientColoredLocation  {

    private String locationType;
    private String locationValue;





    private styles_Color styles_color;


    public mm_styles_GradientColoredLocation(
        String locationType,        String locationValue    ) {
        this.locationType = locationType;
        this.locationValue = locationValue;
    }


    public String getLocationtype() {
        return locationType;
    }

    public void setLocationtype(String locationType) {
        this.locationType = locationType;
    }
    public String getLocationvalue() {
        return locationValue;
    }

    public void setLocationvalue(String locationValue) {
        this.locationValue = locationValue;
    }

    public styles_Color getStyles_color() {
        return styles_color;
    }

    public void setStyles_color(styles_Color styles_color) {
        this.styles_color = styles_color;
    }

}