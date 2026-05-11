





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EStructuralFeature extends ETypedElement {

    private boolean transient;
    private String defaultValueLiteral;
    private boolean volatile;
    private boolean derived;
    private boolean changeable;
    private boolean unsettable;





    private ecoreDiff_EClass ecorediff_eclass;




    private ecoreDiff_ChangedEStructuralFeature ecorediff_changedestructuralfeature;




    private ecoreDiff_EObject ecorediff_eobject;


    public ecoreDiff_EStructuralFeature(
        boolean transient,        String defaultValueLiteral,        boolean volatile,        boolean derived,        boolean changeable,        boolean unsettable    ) {
        super(
        );
        this.transient = transient;
        this.defaultValueLiteral = defaultValueLiteral;
        this.volatile = volatile;
        this.derived = derived;
        this.changeable = changeable;
        this.unsettable = unsettable;
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

    public ecoreDiff_EClass getEcorediff_eclass() {
        return ecorediff_eclass;
    }

    public void setEcorediff_eclass(ecoreDiff_EClass ecorediff_eclass) {
        this.ecorediff_eclass = ecorediff_eclass;
    }
    public ecoreDiff_ChangedEStructuralFeature getEcorediff_changedestructuralfeature() {
        return ecorediff_changedestructuralfeature;
    }

    public void setEcorediff_changedestructuralfeature(ecoreDiff_ChangedEStructuralFeature ecorediff_changedestructuralfeature) {
        this.ecorediff_changedestructuralfeature = ecorediff_changedestructuralfeature;
    }
    public ecoreDiff_EObject getEcorediff_eobject() {
        return ecorediff_eobject;
    }

    public void setEcorediff_eobject(ecoreDiff_EObject ecorediff_eobject) {
        this.ecorediff_eobject = ecorediff_eobject;
    }

}