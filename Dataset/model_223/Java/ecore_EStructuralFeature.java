





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private boolean transient;
    private boolean derived;
    private boolean volatile;
    private boolean unsettable;
    private String defaultValueLiteral;
    private boolean changeable;
    private String defaultValue;



    public ecore_EStructuralFeature(
        boolean transient,        boolean derived,        boolean volatile,        boolean unsettable,        String defaultValueLiteral,        boolean changeable,        String defaultValue    ) {
        super(
        );
        this.transient = transient;
        this.derived = derived;
        this.volatile = volatile;
        this.unsettable = unsettable;
        this.defaultValueLiteral = defaultValueLiteral;
        this.changeable = changeable;
        this.defaultValue = defaultValue;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }
    public boolean getUnsettable() {
        return unsettable;
    }

    public void setUnsettable(boolean unsettable) {
        this.unsettable = unsettable;
    }
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }
    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}