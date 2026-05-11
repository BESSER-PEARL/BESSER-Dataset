





import java.util.List;
import java.util.ArrayList;

public class swt_AbstractMenu extends Widget {

    private boolean enabled;
    private String textOrientationStyle;
    private boolean visible;



    public swt_AbstractMenu(
        boolean enabled,        String textOrientationStyle,        boolean visible    ) {
        super(
        );
        this.enabled = enabled;
        this.textOrientationStyle = textOrientationStyle;
        this.visible = visible;
    }


    public boolean getEnabled() {
        return enabled;
    }

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
    }
    public String getTextorientationstyle() {
        return textOrientationStyle;
    }

    public void setTextorientationstyle(String textOrientationStyle) {
        this.textOrientationStyle = textOrientationStyle;
    }
    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }


}