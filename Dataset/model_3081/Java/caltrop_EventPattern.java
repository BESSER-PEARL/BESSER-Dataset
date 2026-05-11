





import java.util.List;
import java.util.ArrayList;

public class caltrop_EventPattern extends ActionPattern {

    private boolean _property;
    private String name;
    private String variables;
    private String qualifier;





    private caltrop_XExpression caltrop_xexpression;




    private caltrop_XExpression caltrop_xexpression;




    private caltrop_StateVariable caltrop_statevariable;




    private caltrop_EventAction caltrop_eventaction;


    public caltrop_EventPattern(
        boolean _property,        String name,        String variables,        String qualifier    ) {
        super(
        );
        this._property = _property;
        this.name = name;
        this.variables = variables;
        this.qualifier = qualifier;
    }


    public boolean get_property() {
        return _property;
    }

    public void set_property(boolean _property) {
        this._property = _property;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getVariables() {
        return variables;
    }

    public void setVariables(String variables) {
        this.variables = variables;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }

    public caltrop_XExpression getCaltrop_xexpression() {
        return caltrop_xexpression;
    }

    public void setCaltrop_xexpression(caltrop_XExpression caltrop_xexpression) {
        this.caltrop_xexpression = caltrop_xexpression;
    }
    public caltrop_XExpression getCaltrop_xexpression() {
        return caltrop_xexpression;
    }

    public void setCaltrop_xexpression(caltrop_XExpression caltrop_xexpression) {
        this.caltrop_xexpression = caltrop_xexpression;
    }
    public caltrop_StateVariable getCaltrop_statevariable() {
        return caltrop_statevariable;
    }

    public void setCaltrop_statevariable(caltrop_StateVariable caltrop_statevariable) {
        this.caltrop_statevariable = caltrop_statevariable;
    }
    public caltrop_EventAction getCaltrop_eventaction() {
        return caltrop_eventaction;
    }

    public void setCaltrop_eventaction(caltrop_EventAction caltrop_eventaction) {
        this.caltrop_eventaction = caltrop_eventaction;
    }

}