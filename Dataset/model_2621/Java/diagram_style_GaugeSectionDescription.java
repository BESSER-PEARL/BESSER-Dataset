





import java.util.List;
import java.util.ArrayList;

public class diagram_style_GaugeSectionDescription  {

    private String valueExpression;
    private String label;
    private String minValueExpression;
    private String maxValueExpression;





    private ColorDescription colordescription;




    private ColorDescription colordescription;


    public diagram_style_GaugeSectionDescription(
        String valueExpression,        String label,        String minValueExpression,        String maxValueExpression    ) {
        this.valueExpression = valueExpression;
        this.label = label;
        this.minValueExpression = minValueExpression;
        this.maxValueExpression = maxValueExpression;
    }


    public String getValueexpression() {
        return valueExpression;
    }

    public void setValueexpression(String valueExpression) {
        this.valueExpression = valueExpression;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getMinvalueexpression() {
        return minValueExpression;
    }

    public void setMinvalueexpression(String minValueExpression) {
        this.minValueExpression = minValueExpression;
    }
    public String getMaxvalueexpression() {
        return maxValueExpression;
    }

    public void setMaxvalueexpression(String maxValueExpression) {
        this.maxValueExpression = maxValueExpression;
    }

    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }
    public ColorDescription getColordescription() {
        return colordescription;
    }

    public void setColordescription(ColorDescription colordescription) {
        this.colordescription = colordescription;
    }

}