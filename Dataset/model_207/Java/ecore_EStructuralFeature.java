





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private String derived;
    private String defaultValue;
    private String changeable;
    private String defaultValueLiteral;
    private String unsettable;
    private String transient;
    private String volatile;





    private EClass eclass;


    public ecore_EStructuralFeature(
        String derived,        String defaultValue,        String changeable,        String defaultValueLiteral,        String unsettable,        String transient,        String volatile    ) {
        super(
        );
        this.derived = derived;
        this.defaultValue = defaultValue;
        this.changeable = changeable;
        this.defaultValueLiteral = defaultValueLiteral;
        this.unsettable = unsettable;
        this.transient = transient;
        this.volatile = volatile;
    }


    public String getDerived() {
        return derived;
    }

    public void setDerived(String derived) {
        this.derived = derived;
    }
    public String getDefaultvalue() {
        return defaultValue;
    }

    public void setDefaultvalue(String defaultValue) {
        this.defaultValue = defaultValue;
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
    public String getUnsettable() {
        return unsettable;
    }

    public void setUnsettable(String unsettable) {
        this.unsettable = unsettable;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }

    public EClass getEclass() {
        return eclass;
    }

    public void setEclass(EClass eclass) {
        this.eclass = eclass;
    }

}