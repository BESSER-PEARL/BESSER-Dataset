





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private boolean derived;
    private boolean transient;
    private boolean changeable;
    private boolean volatile;
    private boolean unsettable;
    private String defaultValue;
    private String defaultValueLiteral;





    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;


    public ecore_EStructuralFeature(
        boolean derived,        boolean transient,        boolean changeable,        boolean volatile,        boolean unsettable,        String defaultValue,        String defaultValueLiteral    ) {
        super(
        );
        this.derived = derived;
        this.transient = transient;
        this.changeable = changeable;
        this.volatile = volatile;
        this.unsettable = unsettable;
        this.defaultValue = defaultValue;
        this.defaultValueLiteral = defaultValueLiteral;
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
    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
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
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
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