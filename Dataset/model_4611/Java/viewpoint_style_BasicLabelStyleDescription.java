





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_BasicLabelStyleDescription  {

    private int labelSize;
    private String iconPath;
    private String labelExpression;
    private String labelFormat;
    private boolean showIcon;





    private ColorDescription colordescription;


    public viewpoint_style_BasicLabelStyleDescription(
        int labelSize,        String iconPath,        String labelExpression,        String labelFormat,        boolean showIcon    ) {
        this.labelSize = labelSize;
        this.iconPath = iconPath;
        this.labelExpression = labelExpression;
        this.labelFormat = labelFormat;
        this.showIcon = showIcon;
    }


    public int getLabelsize() {
        return labelSize;
    }

    public void setLabelsize(int labelSize) {
        this.labelSize = labelSize;
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
    public String getLabelformat() {
        return labelFormat;
    }

    public void setLabelformat(String labelFormat) {
        this.labelFormat = labelFormat;
    }
    public boolean getShowicon() {
        return showIcon;
    }

    public void setShowicon(boolean showIcon) {
        this.showIcon = showIcon;
    }

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}