





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_BasicLabelStyleDescription  {

    private int labelSize;
    private boolean showIcon;
    private String labelExpression;
    private String iconPath;
    private String labelFormat;





    private ColorDescription colordescription;


    public viewpoint_style_BasicLabelStyleDescription(
        int labelSize,        boolean showIcon,        String labelExpression,        String iconPath,        String labelFormat    ) {
        this.labelSize = labelSize;
        this.showIcon = showIcon;
        this.labelExpression = labelExpression;
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
    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
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

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}