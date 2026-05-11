





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ENamedElement extends EModelElement {

    private String name;





    private ecoreDiff_ChangedENamedElement ecorediff_changedenamedelement;


    public ecoreDiff_ENamedElement(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ecoreDiff_ChangedENamedElement getEcorediff_changedenamedelement() {
        return ecorediff_changedenamedelement;
    }

    public void setEcorediff_changedenamedelement(ecoreDiff_ChangedENamedElement ecorediff_changedenamedelement) {
        this.ecorediff_changedenamedelement = ecorediff_changedenamedelement;
    }

}