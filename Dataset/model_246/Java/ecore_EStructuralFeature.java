





import java.util.List;
import java.util.ArrayList;

public class ecore_EStructuralFeature extends ETypedElement {

    private String defaultValueLiteral;
    private String defaultValue;
    private boolean volatile;
    private boolean transient;
    private boolean derived;
    private boolean unsettable;
    private boolean changeable;





    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;




    private ecore_EClass ecore_eclass;


    public ecore_EStructuralFeature(
        String defaultValueLiteral,        String defaultValue,        boolean volatile,        boolean transient,        boolean derived,        boolean unsettable,        boolean changeable    ) {
        super(
        );
        this.defaultValueLiteral = defaultValueLiteral;
        this.defaultValue = defaultValue;
        this.volatile = volatile;
        this.transient = transient;
        this.derived = derived;
        this.unsettable = unsettable;
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
    public boolean getChangeable() {
        return changeable;
    }

    public void setChangeable(boolean changeable) {
        this.changeable = changeable;
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