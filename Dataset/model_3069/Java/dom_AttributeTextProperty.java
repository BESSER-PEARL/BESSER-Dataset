





import java.util.List;
import java.util.ArrayList;

public class dom_AttributeTextProperty extends AttributeProperty {

    private String tooltipText;
    private String labelText;
    private String unitText;
    private String hstoreColumn;





    private dom_Attribute dom_attribute;


    public dom_AttributeTextProperty(
        String tooltipText,        String labelText,        String unitText,        String hstoreColumn    ) {
        super(
        );
        this.tooltipText = tooltipText;
        this.labelText = labelText;
        this.unitText = unitText;
        this.hstoreColumn = hstoreColumn;
    }


    public String getTooltiptext() {
        return tooltipText;
    }

    public void setTooltiptext(String tooltipText) {
        this.tooltipText = tooltipText;
    }
    public String getLabeltext() {
        return labelText;
    }

    public void setLabeltext(String labelText) {
        this.labelText = labelText;
    }
    public String getUnittext() {
        return unitText;
    }

    public void setUnittext(String unitText) {
        this.unitText = unitText;
    }
    public String getHstorecolumn() {
        return hstoreColumn;
    }

    public void setHstorecolumn(String hstoreColumn) {
        this.hstoreColumn = hstoreColumn;
    }

    public dom_Attribute getDom_attribute() {
        return dom_attribute;
    }

    public void setDom_attribute(dom_Attribute dom_attribute) {
        this.dom_attribute = dom_attribute;
    }

}