





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ETypedElement extends ENamedElement {

    private boolean unique;
    private int lowerBound;
    private int upperBound;
    private boolean ordered;





    private ecoreDiff_ChangedETypedElement ecorediff_changedetypedelement;




    private ecoreDiff_EObject ecorediff_eobject;


    public ecoreDiff_ETypedElement(
        boolean unique,        int lowerBound,        int upperBound,        boolean ordered    ) {
        super(
        );
        this.unique = unique;
        this.lowerBound = lowerBound;
        this.upperBound = upperBound;
        this.ordered = ordered;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }
    public int getLowerbound() {
        return lowerBound;
    }

    public void setLowerbound(int lowerBound) {
        this.lowerBound = lowerBound;
    }
    public int getUpperbound() {
        return upperBound;
    }

    public void setUpperbound(int upperBound) {
        this.upperBound = upperBound;
    }
    public boolean getOrdered() {
        return ordered;
    }

    public void setOrdered(boolean ordered) {
        this.ordered = ordered;
    }

    public ecoreDiff_ChangedETypedElement getEcorediff_changedetypedelement() {
        return ecorediff_changedetypedelement;
    }

    public void setEcorediff_changedetypedelement(ecoreDiff_ChangedETypedElement ecorediff_changedetypedelement) {
        this.ecorediff_changedetypedelement = ecorediff_changedetypedelement;
    }
    public ecoreDiff_EObject getEcorediff_eobject() {
        return ecorediff_eobject;
    }

    public void setEcorediff_eobject(ecoreDiff_EObject ecorediff_eobject) {
        this.ecorediff_eobject = ecorediff_eobject;
    }

}