





import java.util.List;
import java.util.ArrayList;

public class viewpoint_BasicLabelStyle extends Customizable {

    private int labelSize;
    private boolean showIcon;
    private String iconPath;
    private String labelFormat;



    public viewpoint_BasicLabelStyle(
        int labelSize,        boolean showIcon,        String iconPath,        String labelFormat    ) {
        super(
        );
        this.labelSize = labelSize;
        this.showIcon = showIcon;
        this.iconPath = iconPath;
        this.labelFormat = labelFormat;
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


}