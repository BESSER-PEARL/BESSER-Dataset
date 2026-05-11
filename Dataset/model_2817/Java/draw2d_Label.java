





import java.util.List;
import java.util.ArrayList;

public class draw2d_Label extends Figure {

    private String text;
    private String textPlacement;
    private String textAlignment;
    private String iconAlignment;
    private int iconTextGap;
    private String icon;



    public draw2d_Label(
        String text,        String textPlacement,        String textAlignment,        String iconAlignment,        int iconTextGap,        String icon    ) {
        super(
        );
        this.text = text;
        this.textPlacement = textPlacement;
        this.textAlignment = textAlignment;
        this.iconAlignment = iconAlignment;
        this.iconTextGap = iconTextGap;
        this.icon = icon;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public String getTextplacement() {
        return textPlacement;
    }

    public void setTextplacement(String textPlacement) {
        this.textPlacement = textPlacement;
    }
    public String getTextalignment() {
        return textAlignment;
    }

    public void setTextalignment(String textAlignment) {
        this.textAlignment = textAlignment;
    }
    public String getIconalignment() {
        return iconAlignment;
    }

    public void setIconalignment(String iconAlignment) {
        this.iconAlignment = iconAlignment;
    }
    public int getIcontextgap() {
        return iconTextGap;
    }

    public void setIcontextgap(int iconTextGap) {
        this.iconTextGap = iconTextGap;
    }
    public String getIcon() {
        return icon;
    }

    public void setIcon(String icon) {
        this.icon = icon;
    }


}