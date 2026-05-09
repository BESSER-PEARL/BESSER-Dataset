





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private String defaultValueLiteral;
    private String defaultValue;
    private String volatile;
    private String derived;
    private String changeable;
    private String transient;
    private String unsettable;





    private EClass eclass;


    public ecore_EStructuralFeature(
        String defaultValueLiteral,        String defaultValue,        String volatile,        String derived,        String changeable,        String transient,        String unsettable    ) {
        super(
        );
        this.defaultValueLiteral = defaultValueLiteral;
        this.defaultValue = defaultValue;
        this.volatile = volatile;
        this.derived = derived;
        this.changeable = changeable;
        this.transient = transient;
        this.unsettable = unsettable;
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
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getDerived() {
        return derived;
    }

    public void setDerived(String derived) {
        this.derived = derived;
    }
    public String getChangeable() {
        return changeable;
    }

    public void setChangeable(String changeable) {
        this.changeable = changeable;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }
    public String getUnsettable() {
        return unsettable;
    }

    public void setUnsettable(String unsettable) {
        this.unsettable = unsettable;
    }

    public EClass getEclass() {
        return eclass;
    }

    public void setEclass(EClass eclass) {
        this.eclass = eclass;
    }

}