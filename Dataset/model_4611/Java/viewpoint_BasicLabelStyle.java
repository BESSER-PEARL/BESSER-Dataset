





import java.util.List;
import java.util.ArrayList;

public class viewpoint_BasicLabelStyle extends Customizable {

    private boolean showIcon;
    private String iconPath;
    private String labelFormat;
    private String labelColor;
    private int labelSize;



    public viewpoint_BasicLabelStyle(
        boolean showIcon,        String iconPath,        String labelFormat,        String labelColor,        int labelSize    ) {
        super(
        );
        this.showIcon = showIcon;
        this.iconPath = iconPath;
        this.labelFormat = labelFormat;
        this.labelColor = labelColor;
        this.labelSize = labelSize;
    }


    public boolean getShowicon() {
        return showIcon;
    }

    public void setShowicon(boolean showIcon) {
        this.showIcon = showIcon;
    }
    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }
    public String getLabelformat() {
        return labelFormat;
    }

    public void setLabelformat(String labelFormat) {
        this.labelFormat = labelFormat;
    }
    public String getLabelcolor() {
        return labelColor;
    }

    public void setLabelcolor(String labelColor) {
        this.labelColor = labelColor;
    }
    public int getLabelsize() {
        return labelSize;
    }

    public void setLabelsize(int labelSize) {
        this.labelSize = labelSize;
    }


}