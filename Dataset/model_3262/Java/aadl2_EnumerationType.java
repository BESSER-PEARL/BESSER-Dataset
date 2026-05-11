





import java.util.List;
import java.util.ArrayList;

public class aadl2_EnumerationType extends NonListType, Namespace {






    private List<aadl2_EnumerationLiteral> aadl2_enumerationliterals;


    public aadl2_EnumerationType(
    ) {
        super(
        );
        this.aadl2_enumerationliterals = new ArrayList<>();
    }

    public aadl2_EnumerationType(
        ArrayList<aadl2_EnumerationLiteral> aadl2_enumerationliterals    ) {
        this.aadl2_enumerationliterals = aadl2_enumerationliterals;
    }


    public List<aadl2_EnumerationLiteral> getAadl2_enumerationliterals() {
        return aadl2_enumerationliterals;
    }

    public void addAadl2_enumerationliteral(Aadl2_enumerationliteral aadl2_enumerationliteral) {
        this.aadl2_enumerationliterals.add(aadl2_enumerationliteral);
    }

}