





import java.util.List;
import java.util.ArrayList;

public class viewpoint_BasicLabelStyle extends Customizable {

    private String labelColor;
    private boolean showIcon;
    private String labelFormat;
    private String iconPath;
    private int labelSize;



    public viewpoint_BasicLabelStyle(
        String labelColor,        boolean showIcon,        String labelFormat,        String iconPath,        int labelSize    ) {
        super(
        );
        this.labelColor = labelColor;
        this.showIcon = showIcon;
        this.labelFormat = labelFormat;
        this.iconPath = iconPath;
        this.labelSize = labelSize;
    }


    public String getLabelcolor() {
        return labelColor;
    }

    public void setLabelcolor(String labelColor) {
        this.labelColor = labelColor;
    }
    public boolean getShowicon() {
        return showIcon;
    }

    public void setShowicon(boolean showIcon) {
        this.showIcon = showIcon;
    }
    public String getLabelformat() {
        return labelFormat;
    }

    public void setLabelformat(String labelFormat) {
        this.labelFormat = labelFormat;
    }
    public String getIconpath() {
        return iconPath;
    }

    public void setIconpath(String iconPath) {
        this.iconPath = iconPath;
    }
    public int getLabelsize() {
        return labelSize;
    }

    public void setLabelsize(int labelSize) {
        this.labelSize = labelSize;
    }


}