





import java.util.List;
import java.util.ArrayList;

public class yuml_Relationship extends ModelElement {

    private String targetLabel;
    private String sourceLabel;





    private yuml_ColorableElement yuml_colorableelement;




    private yuml_Class yuml_class;


    public yuml_Relationship(
        String targetLabel,        String sourceLabel    ) {
        super(
        );
        this.targetLabel = targetLabel;
        this.sourceLabel = sourceLabel;
    }


    public String getTargetlabel() {
        return targetLabel;
    }

    public void setTargetlabel(String targetLabel) {
        this.targetLabel = targetLabel;
    }
    public String getSourcelabel() {
        return sourceLabel;
    }

    public void setSourcelabel(String sourceLabel) {
        this.sourceLabel = sourceLabel;
    }

    public yuml_ColorableElement getYuml_colorableelement() {
        return yuml_colorableelement;
    }

    public void setYuml_colorableelement(yuml_ColorableElement yuml_colorableelement) {
        this.yuml_colorableelement = yuml_colorableelement;
    }
    public yuml_Class getYuml_class() {
        return yuml_class;
    }

    public void setYuml_class(yuml_Class yuml_class) {
        this.yuml_class = yuml_class;
    }

}