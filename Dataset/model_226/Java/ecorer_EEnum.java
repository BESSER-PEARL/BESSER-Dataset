





import java.util.List;
import java.util.ArrayList;

public class ecorer_EEnum extends EDataType {






    private List<ecorer_EEnumLiteral> ecorer_eenumliterals;




    private ecorer_EEnumLiteral ecorer_eenumliteral;


    public ecorer_EEnum(
    ) {
        super(
        );
        this.ecorer_eenumliterals = new ArrayList<>();
    }

    public ecorer_EEnum(
        ArrayList<ecorer_EEnumLiteral> ecorer_eenumliterals    ) {
        this.ecorer_eenumliterals = ecorer_eenumliterals;
    }


    public List<ecorer_EEnumLiteral> getEcorer_eenumliterals() {
        return ecorer_eenumliterals;
    }

    public void addEcorer_eenumliteral(Ecorer_eenumliteral ecorer_eenumliteral) {
        this.ecorer_eenumliterals.add(ecorer_eenumliteral);
    }
    public ecorer_EEnumLiteral getEcorer_eenumliteral() {
        return ecorer_eenumliteral;
    }

    public void setEcorer_eenumliteral(ecorer_EEnumLiteral ecorer_eenumliteral) {
        this.ecorer_eenumliteral = ecorer_eenumliteral;
    }

}