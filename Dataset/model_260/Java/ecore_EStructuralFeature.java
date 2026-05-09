





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private boolean volatile;
    private boolean transient;
    private boolean unsettable;
    private boolean changeable;
    private String defaultValueLiteral;
    private boolean derived;
    private String defaultValue;



    public ecore_EStructuralFeature(
        boolean volatile,        boolean transient,        boolean unsettable,        boolean changeable,        String defaultValueLiteral,        boolean derived,        String defaultValue    ) {
        super(
        );
        this.volatile = volatile;
        this.transient = transient;
        this.unsettable = unsettable;
        this.changeable = changeable;
        this.defaultValueLiteral = defaultValueLiteral;
        this.derived = derived;
        this.defaultValue = defaultValue;
    }


    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
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
    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
    }
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }


}