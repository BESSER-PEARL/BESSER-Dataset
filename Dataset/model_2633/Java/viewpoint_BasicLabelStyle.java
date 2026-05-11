





import java.util.List;
import java.util.ArrayList;

public class viewpoint_BasicLabelStyle extends Customizable {

    private String labelFormat;
    private String iconPath;
    private int labelSize;
    private boolean showIcon;



    public viewpoint_BasicLabelStyle(
        String labelFormat,        String iconPath,        int labelSize,        boolean showIcon    ) {
        super(
        );
        this.labelFormat = labelFormat;
        this.iconPath = iconPath;
        this.labelSize = labelSize;
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
    public boolean getShowicon() {
        return showIcon;
    }

    public void setShowicon(boolean showIcon) {
        this.showIcon = showIcon;
    }


}