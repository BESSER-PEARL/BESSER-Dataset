





import java.util.List;
import java.util.ArrayList;

public class diagram_style_GaugeSectionDescription  {

    private String minValueExpression;
    private String label;
    private String valueExpression;
    private String maxValueExpression;





    private ColorDescription colordescription;




    private ColorDescription colordescription;


    public diagram_style_GaugeSectionDescription(
        String minValueExpression,        String label,        String valueExpression,        String maxValueExpression    ) {
        this.minValueExpression = minValueExpression;
        this.label = label;
        this.valueExpression = valueExpression;
        this.maxValueExpression = maxValueExpression;
    }


    public String getMinvalueexpression() {
        return minValueExpression;
    }

    public void setMinvalueexpression(String minValueExpression) {
        this.minValueExpression = minValueExpression;
    }
    public String getLabel() {
        return label;
    }

    public void setLabel(String label) {
        this.label = label;
    }
    public String getValueexpression() {
        return valueExpression;
    }

    public void setValueexpression(String valueExpression) {
        this.valueExpression = valueExpression;
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