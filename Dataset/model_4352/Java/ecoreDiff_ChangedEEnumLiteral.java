





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_ChangedEEnumLiteral extends EEnumLiteral {






    private List<ecoreDiff_EEnumLiteral> ecorediff_eenumliterals;




    private ecoreDiff_EObject ecorediff_eobject;


    public ecoreDiff_ChangedEEnumLiteral(
    ) {
        super(
        );
        this.ecorediff_eenumliterals = new ArrayList<>();
    }

    public ecoreDiff_ChangedEEnumLiteral(
        ArrayList<ecoreDiff_EEnumLiteral> ecorediff_eenumliterals    ) {
        this.ecorediff_eenumliterals = ecorediff_eenumliterals;
    }


    public List<ecoreDiff_EEnumLiteral> getEcorediff_eenumliterals() {
        return ecorediff_eenumliterals;
    }

    public void addEcorediff_eenumliteral(Ecorediff_eenumliteral ecorediff_eenumliteral) {
        this.ecorediff_eenumliterals.add(ecorediff_eenumliteral);
    }
    public ecoreDiff_EObject getEcorediff_eobject() {
        return ecorediff_eobject;
    }

    public void setEcorediff_eobject(ecoreDiff_EObject ecorediff_eobject) {
        this.ecorediff_eobject = ecorediff_eobject;
    }

}