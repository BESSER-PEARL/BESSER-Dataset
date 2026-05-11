





import java.util.List;
import java.util.ArrayList;

public class viewpoint_style_BasicLabelStyleDescription  {

    private String iconPath;
    private String labelFormat;
    private int labelSize;
    private String labelExpression;
    private boolean showIcon;





    private ColorDescription colordescription;


    public viewpoint_style_BasicLabelStyleDescription(
        String iconPath,        String labelFormat,        int labelSize,        String labelExpression,        boolean showIcon    ) {
        this.iconPath = iconPath;
        this.labelFormat = labelFormat;
        this.labelSize = labelSize;
        this.labelExpression = labelExpression;
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
    public int getLabelsize() {
        return labelSize;
    }

    public void setLabelsize(int labelSize) {
        this.labelSize = labelSize;
    }
    public String getLabelexpression() {
        return labelExpression;
    }

    public void setLabelexpression(String labelExpression) {
        this.labelExpression = labelExpression;
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