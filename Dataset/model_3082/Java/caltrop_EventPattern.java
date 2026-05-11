





import java.util.List;
import java.util.ArrayList;

public class caltrop_EventPattern extends ActionPattern {

    private String qualifier;
    private String name;
    private String variables;
    private boolean _property;





    private caltrop_StateVariable caltrop_statevariable;




    private caltrop_EventAction caltrop_eventaction;


    public caltrop_EventPattern(
        String qualifier,        String name,        String variables,        boolean _property    ) {
        super(
        );
        this.qualifier = qualifier;
        this.name = name;
        this.variables = variables;
        this._property = _property;
    }


    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
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
    public boolean get_property() {
        return _property;
    }

    public void set_property(boolean _property) {
        this._property = _property;
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