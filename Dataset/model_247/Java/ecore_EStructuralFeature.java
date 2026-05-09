





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private boolean changeable;
    private boolean unsettable;
    private String defaultValue;
    private String defaultValueLiteral;
    private boolean volatile;
    private boolean derived;
    private boolean transient;





    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;


    public ecore_EStructuralFeature(
        boolean changeable,        boolean unsettable,        String defaultValue,        String defaultValueLiteral,        boolean volatile,        boolean derived,        boolean transient    ) {
        super(
        );
        this.changeable = changeable;
        this.unsettable = unsettable;
        this.defaultValue = defaultValue;
        this.defaultValueLiteral = defaultValueLiteral;
        this.volatile = volatile;
        this.derived = derived;
        this.transient = transient;
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
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
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
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }

    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }
    public ecore_EClass getEcore_eclass() {
        return ecore_eclass;
    }

    public void setEcore_eclass(ecore_EClass ecore_eclass) {
        this.ecore_eclass = ecore_eclass;
    }

}