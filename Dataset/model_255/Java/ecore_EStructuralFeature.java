





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private boolean transient;
    private boolean unsettable;
    private boolean derived;
    private boolean changeable;
    private String defaultValue;
    private boolean volatile;
    private String defaultValueLiteral;



    public ecore_EStructuralFeature(
        boolean transient,        boolean unsettable,        boolean derived,        boolean changeable,        String defaultValue,        boolean volatile,        String defaultValueLiteral    ) {
        super(
        );
        this.transient = transient;
        this.unsettable = unsettable;
        this.derived = derived;
        this.changeable = changeable;
        this.defaultValue = defaultValue;
        this.volatile = volatile;
        this.defaultValueLiteral = defaultValueLiteral;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getUnsettable() {
        return unsettable;
    }

    public void setUnsettable(boolean unsettable) {
        this.unsettable = unsettable;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
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
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }


}