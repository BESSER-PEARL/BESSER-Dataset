





import java.util.List;
import java.util.ArrayList;

public class model_IconSupport  {

    private String icon;
    private String iconRotation;



    public model_IconSupport(
        String icon,        String iconRotation    ) {
        this.icon = icon;
        this.iconRotation = iconRotation;
    }


    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }
    public String getIconrotation() {
        return iconRotation;
    }

    public void setIconrotation(String iconRotation) {
        this.iconRotation = iconRotation;
    }


}