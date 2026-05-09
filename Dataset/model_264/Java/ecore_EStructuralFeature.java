





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private boolean volatile;
    private boolean derived;
    private String defaultValueLiteral;
    private boolean changeable;
    private boolean unsettable;
    private String defaultValue;
    private boolean transient;



    public ecore_EStructuralFeature(
        boolean volatile,        boolean derived,        String defaultValueLiteral,        boolean changeable,        boolean unsettable,        String defaultValue,        boolean transient    ) {
        super(
        );
        this.volatile = volatile;
        this.derived = derived;
        this.defaultValueLiteral = defaultValueLiteral;
        this.changeable = changeable;
        this.unsettable = unsettable;
        this.defaultValue = defaultValue;
        this.transient = transient;
    }


    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
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
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }


}