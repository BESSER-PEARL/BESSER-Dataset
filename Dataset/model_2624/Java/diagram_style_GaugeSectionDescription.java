





import java.util.List;
import java.util.ArrayList;

public class diagram_style_GaugeSectionDescription  {

    private String maxValueExpression;
    private String valueExpression;
    private String minValueExpression;
    private String label;





    private ColorDescription colordescription;




    private ColorDescription colordescription;


    public diagram_style_GaugeSectionDescription(
        String maxValueExpression,        String valueExpression,        String minValueExpression,        String label    ) {
        this.maxValueExpression = maxValueExpression;
        this.valueExpression = valueExpression;
        this.minValueExpression = minValueExpression;
        this.label = label;
    }


    public String getMaxvalueexpression() {
        return maxValueExpression;
    }

    public void setMaxvalueexpression(String maxValueExpression) {
        this.maxValueExpression = maxValueExpression;
    }
    public String getValueexpression() {
        return valueExpression;
    }

    public void setValueexpression(String valueExpression) {
        this.valueExpression = valueExpression;
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