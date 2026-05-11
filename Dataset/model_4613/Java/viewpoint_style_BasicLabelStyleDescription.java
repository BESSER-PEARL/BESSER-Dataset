





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_BasicLabelStyleDescription  {

    private String labelFormat;
    private int labelSize;
    private boolean showIcon;
    private String iconPath;
    private String labelExpression;





    private ColorDescription colordescription;


    public viewpoint_style_BasicLabelStyleDescription(
        String labelFormat,        int labelSize,        boolean showIcon,        String iconPath,        String labelExpression    ) {
        this.labelFormat = labelFormat;
        this.labelSize = labelSize;
        this.showIcon = showIcon;
        this.iconPath = iconPath;
        this.labelExpression = labelExpression;
    }


    public String getLabelformat() {
        return labelFormat;
    }

    public void setLabelformat(String labelFormat) {
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
    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
    }

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}