





import java.util.List;
import java.util.ArrayList;

public class encore_EStructuralFeature extends ETypedElement {

    private boolean transient;
    private String defaultValue;
    private boolean changeable;
    private boolean unsettable;
    private boolean volatile;
    private String defaultValueLiteral;
    private boolean derived;



    public encore_EStructuralFeature(
        boolean transient,        String defaultValue,        boolean changeable,        boolean unsettable,        boolean volatile,        String defaultValueLiteral,        boolean derived    ) {
        super(
        );
        this.transient = transient;
        this.defaultValue = defaultValue;
        this.changeable = changeable;
        this.unsettable = unsettable;
        this.volatile = volatile;
        this.defaultValueLiteral = defaultValueLiteral;
        this.derived = derived;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
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
    public boolean getDerived() {
        return derived;
    }

    public void setDerived(boolean derived) {
        this.derived = derived;
    }


}