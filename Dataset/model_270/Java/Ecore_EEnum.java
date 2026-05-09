





import java.util.List;
import java.util.ArrayList;

public class Ecore_EEnum extends EDataType {






    private List<Ecore_EEnumLiteral> ecore_eenumliterals;




    private Ecore_EEnumLiteral ecore_eenumliteral;


    public Ecore_EEnum(
    ) {
        super(
        );
        this.ecore_eenumliterals = new ArrayList<>();
    }

    public Ecore_EEnum(
        ArrayList<Ecore_EEnumLiteral> ecore_eenumliterals    ) {
        this.ecore_eenumliterals = ecore_eenumliterals;
    }


    public List<Ecore_EEnumLiteral> getEcore_eenumliterals() {
        return ecore_eenumliterals;
    }

    public void addEcore_eenumliteral(Ecore_eenumliteral ecore_eenumliteral) {
        this.ecore_eenumliterals.add(ecore_eenumliteral);
    }
    public Ecore_EEnumLiteral getEcore_eenumliteral() {
        return ecore_eenumliteral;
    }

    public void setEcore_eenumliteral(Ecore_EEnumLiteral ecore_eenumliteral) {
        this.ecore_eenumliteral = ecore_eenumliteral;
    }

}