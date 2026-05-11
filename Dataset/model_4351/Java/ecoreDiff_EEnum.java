





import java.util.List;
import java.util.ArrayList;

public class ecoreDiff_EEnum extends EDataType {






    private ecoreDiff_EEnumLiteral ecorediff_eenumliteral;




    private List<ecoreDiff_EEnumLiteral> ecorediff_eenumliterals;


    public ecoreDiff_EEnum(
    ) {
        super(
        );
        this.ecorediff_eenumliterals = new ArrayList<>();
    }

    public ecoreDiff_EEnum(
        ArrayList<ecoreDiff_EEnumLiteral> ecorediff_eenumliterals    ) {
        this.ecorediff_eenumliterals = ecorediff_eenumliterals;
    }


    public ecoreDiff_EEnumLiteral getEcorediff_eenumliteral() {
        return ecorediff_eenumliteral;
    }

    public void setEcorediff_eenumliteral(ecoreDiff_EEnumLiteral ecorediff_eenumliteral) {
        this.ecorediff_eenumliteral = ecorediff_eenumliteral;
    }
    public List<ecoreDiff_EEnumLiteral> getEcorediff_eenumliterals() {
        return ecorediff_eenumliterals;
    }

    public void addEcorediff_eenumliteral(Ecorediff_eenumliteral ecorediff_eenumliteral) {
        this.ecorediff_eenumliterals.add(ecorediff_eenumliteral);
    }

}