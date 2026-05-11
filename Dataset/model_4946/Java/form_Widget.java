





import java.util.List;
import java.util.ArrayList;

public class form_Widget extends Element, CSSCustomizable {

    private String version;
    private boolean mandatory;
    private boolean injectWidgetCondition;
    private boolean displayDependentWidgetOnlyOnEventTriggered;
    private String realHtmlAttributes;
    private String labelPosition;
    private boolean readOnly;
    private String showDisplayLabel;
    private boolean allowHTMLForDisplayLabel;
    private String returnTypeModifier;





    private List<form_WidgetDependency> form_widgetdependencys;




    private List<form_WidgetDependency> form_widgetdependencys;




    private form_WidgetDependency form_widgetdependency;


    public form_Widget(
        String version,        boolean mandatory,        boolean injectWidgetCondition,        boolean displayDependentWidgetOnlyOnEventTriggered,        String realHtmlAttributes,        String labelPosition,        boolean readOnly,        String showDisplayLabel,        boolean allowHTMLForDisplayLabel,        String returnTypeModifier    ) {
        super(
        );
        this.version = version;
        this.mandatory = mandatory;
        this.injectWidgetCondition = injectWidgetCondition;
        this.displayDependentWidgetOnlyOnEventTriggered = displayDependentWidgetOnlyOnEventTriggered;
        this.realHtmlAttributes = realHtmlAttributes;
        this.labelPosition = labelPosition;
        this.readOnly = readOnly;
        this.showDisplayLabel = showDisplayLabel;
        this.allowHTMLForDisplayLabel = allowHTMLForDisplayLabel;
        this.returnTypeModifier = returnTypeModifier;
        this.form_widgetdependencys = new ArrayList<>();
        this.form_widgetdependencys = new ArrayList<>();
    }

    public form_Widget(
        String version,        boolean mandatory,        boolean injectWidgetCondition,        boolean displayDependentWidgetOnlyOnEventTriggered,        String realHtmlAttributes,        String labelPosition,        boolean readOnly,        String showDisplayLabel,        boolean allowHTMLForDisplayLabel,        String returnTypeModifier        ArrayList<form_WidgetDependency> form_widgetdependencys,        ArrayList<form_WidgetDependency> form_widgetdependencys    ) {
        this.version = version;
        this.mandatory = mandatory;
        this.injectWidgetCondition = injectWidgetCondition;
        this.displayDependentWidgetOnlyOnEventTriggered = displayDependentWidgetOnlyOnEventTriggered;
        this.realHtmlAttributes = realHtmlAttributes;
        this.labelPosition = labelPosition;
        this.readOnly = readOnly;
        this.showDisplayLabel = showDisplayLabel;
        this.allowHTMLForDisplayLabel = allowHTMLForDisplayLabel;
        this.returnTypeModifier = returnTypeModifier;
        this.form_widgetdependencys = form_widgetdependencys;
        this.form_widgetdependencys = form_widgetdependencys;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public boolean getMandatory() {
        return mandatory;
    }

    public void setMandatory(boolean mandatory) {
        this.mandatory = mandatory;
    }
    public boolean getInjectwidgetcondition() {
        return injectWidgetCondition;
    }

    public void setInjectwidgetcondition(boolean injectWidgetCondition) {
        this.injectWidgetCondition = injectWidgetCondition;
    }
    public boolean getDisplaydependentwidgetonlyoneventtriggered() {
        return displayDependentWidgetOnlyOnEventTriggered;
    }

    public void setDisplaydependentwidgetonlyoneventtriggered(boolean displayDependentWidgetOnlyOnEventTriggered) {
        this.displayDependentWidgetOnlyOnEventTriggered = displayDependentWidgetOnlyOnEventTriggered;
    }
    public String getRealhtmlattributes() {
        return realHtmlAttributes;
    }

    public void setRealhtmlattributes(String realHtmlAttributes) {
        this.realHtmlAttributes = realHtmlAttributes;
    }
    public String getLabelposition() {
        return labelPosition;
    }

    public void setLabelposition(String labelPosition) {
        this.labelPosition = labelPosition;
    }
    public boolean getReadonly() {
        return readOnly;
    }

    public void setReadonly(boolean readOnly) {
        this.readOnly = readOnly;
    }
    public String getShowdisplaylabel() {
        return showDisplayLabel;
    }

    public void setShowdisplaylabel(String showDisplayLabel) {
        this.showDisplayLabel = showDisplayLabel;
    }
    public boolean getAllowhtmlfordisplaylabel() {
        return allowHTMLForDisplayLabel;
    }

    public void setAllowhtmlfordisplaylabel(boolean allowHTMLForDisplayLabel) {
        this.allowHTMLForDisplayLabel = allowHTMLForDisplayLabel;
    }
    public String getReturntypemodifier() {
        return returnTypeModifier;
    }

    public void setReturntypemodifier(String returnTypeModifier) {
        this.returnTypeModifier = returnTypeModifier;
    }

    public List<form_WidgetDependency> getForm_widgetdependencys() {
        return form_widgetdependencys;
    }

    public void addForm_widgetdependency(Form_widgetdependency form_widgetdependency) {
        this.form_widgetdependencys.add(form_widgetdependency);
    }
    public List<form_WidgetDependency> getForm_widgetdependencys() {
        return form_widgetdependencys;
    }

    public void addForm_widgetdependency(Form_widgetdependency form_widgetdependency) {
        this.form_widgetdependencys.add(form_widgetdependency);
    }
    public form_WidgetDependency getForm_widgetdependency() {
        return form_widgetdependency;
    }

    public void setForm_widgetdependency(form_WidgetDependency form_widgetdependency) {
        this.form_widgetdependency = form_widgetdependency;
    }

}