





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private boolean volatile;
    private boolean unsettable;
    private String defaultValue;
    private boolean derived;
    private String defaultValueLiteral;
    private boolean changeable;
    private boolean transient;



    public ecore_EStructuralFeature(
        boolean volatile,        boolean unsettable,        String defaultValue,        boolean derived,        String defaultValueLiteral,        boolean changeable,        boolean transient    ) {
        super(
        );
        this.volatile = volatile;
        this.unsettable = unsettable;
        this.defaultValue = defaultValue;
        this.derived = derived;
        this.defaultValueLiteral = defaultValueLiteral;
        this.changeable = changeable;
        this.transient = transient;
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
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
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
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }


}