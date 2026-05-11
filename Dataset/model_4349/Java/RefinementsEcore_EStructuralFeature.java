





import java.util.List;
import java.util.ArrayList;

public class RefinementsEcore_EStructuralFeature extends ETypedElement {

    private boolean volatile;
    private boolean changeable;
    private boolean transient;
    private String defaultValueLiteral;
    private boolean derived;
    private boolean unsettable;



    public RefinementsEcore_EStructuralFeature(
        boolean volatile,        boolean changeable,        boolean transient,        String defaultValueLiteral,        boolean derived,        boolean unsettable    ) {
        super(
        );
        this.volatile = volatile;
        this.changeable = changeable;
        this.transient = transient;
        this.defaultValueLiteral = defaultValueLiteral;
        this.derived = derived;
        this.unsettable = unsettable;
    }


    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
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
    public boolean getUnsettable() {
        return unsettable;
    }

    public void setUnsettable(boolean unsettable) {
        this.unsettable = unsettable;
    }


}