





import java.util.List;
import java.util.ArrayList;

public class ecoreO_EEnum extends EDataType {






    private ecoreO_EEnumLiteral ecoreo_eenumliteral;




    private List<ecoreO_EEnumLiteral> ecoreo_eenumliterals;


    public ecoreO_EEnum(
    ) {
        super(
        );
        this.ecoreo_eenumliterals = new ArrayList<>();
    }

    public ecoreO_EEnum(
        ArrayList<ecoreO_EEnumLiteral> ecoreo_eenumliterals    ) {
        this.ecoreo_eenumliterals = ecoreo_eenumliterals;
    }


    public ecoreO_EEnumLiteral getEcoreo_eenumliteral() {
        return ecoreo_eenumliteral;
    }

    public void setEcoreo_eenumliteral(ecoreO_EEnumLiteral ecoreo_eenumliteral) {
        this.ecoreo_eenumliteral = ecoreo_eenumliteral;
    }
    public List<ecoreO_EEnumLiteral> getEcoreo_eenumliterals() {
        return ecoreo_eenumliterals;
    }

    public void addEcoreo_eenumliteral(Ecoreo_eenumliteral ecoreo_eenumliteral) {
        this.ecoreo_eenumliterals.add(ecoreo_eenumliteral);
    }

}