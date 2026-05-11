





import java.util.List;
import java.util.ArrayList;

public class model_IconSupport  {

    private String iconRotation;
    private String icon;



    public model_IconSupport(
        String iconRotation,        String icon    ) {
        this.iconRotation = iconRotation;
        this.icon = icon;
    }


    public String getIconrotation() {
        return iconRotation;
    }

    public void setIconrotation(String iconRotation) {
        this.iconRotation = iconRotation;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }


}