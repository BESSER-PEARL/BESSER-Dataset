





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private String volatile;
    private String unsettable;
    private String derived;
    private String transient;
    private String changeable;
    private String defaultValueLiteral;
    private String defaultValue;





    private EClass eclass;


    public ecore_EStructuralFeature(
        String volatile,        String unsettable,        String derived,        String transient,        String changeable,        String defaultValueLiteral,        String defaultValue    ) {
        super(
        );
        this.volatile = volatile;
        this.unsettable = unsettable;
        this.derived = derived;
        this.transient = transient;
        this.changeable = changeable;
        this.defaultValueLiteral = defaultValueLiteral;
        this.defaultValue = defaultValue;
    }


    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getUnsettable() {
        return unsettable;
    }

    public void setUnsettable(String unsettable) {
        this.unsettable = unsettable;
    }
    public String getDerived() {
        return derived;
    }

    public void setDerived(String derived) {
        this.derived = derived;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }
    public String getChangeable() {
        return changeable;
    }

    public void setChangeable(String changeable) {
        this.changeable = changeable;
    }
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
    }

    public EClass getEclass() {
        return eclass;
    }

    public void setEclass(EClass eclass) {
        this.eclass = eclass;
    }

}