





import java.util.List;
import java.util.ArrayList;

public class ecore_EEnum extends EDataType {






    private List<ecore_EEnumLiteral> ecore_eenumliterals;




    private ecore_EEnumLiteral ecore_eenumliteral;


    public ecore_EEnum(
    ) {
        super(
        );
        this.ecore_eenumliterals = new ArrayList<>();
    }

    public ecore_EEnum(
        ArrayList<ecore_EEnumLiteral> ecore_eenumliterals    ) {
        this.ecore_eenumliterals = ecore_eenumliterals;
    }


    public List<ecore_EEnumLiteral> getEcore_eenumliterals() {
        return ecore_eenumliterals;
    }

    public void addEcore_eenumliteral(Ecore_eenumliteral ecore_eenumliteral) {
        this.ecore_eenumliterals.add(ecore_eenumliteral);
    }
    public ecore_EEnumLiteral getEcore_eenumliteral() {
        return ecore_eenumliteral;
    }

    public void setEcore_eenumliteral(ecore_EEnumLiteral ecore_eenumliteral) {
        this.ecore_eenumliteral = ecore_eenumliteral;
    }

}