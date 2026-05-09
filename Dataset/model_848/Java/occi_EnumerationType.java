





import java.util.List;
import java.util.ArrayList;

public class occi_EnumerationType extends DataType {






    private List<occi_EnumerationLiteral> occi_enumerationliterals;




    private occi_EnumerationLiteral occi_enumerationliteral;


    public occi_EnumerationType(
    ) {
        super(
        );
        this.occi_enumerationliterals = new ArrayList<>();
    }

    public occi_EnumerationType(
        ArrayList<occi_EnumerationLiteral> occi_enumerationliterals    ) {
        this.occi_enumerationliterals = occi_enumerationliterals;
    }


    public List<occi_EnumerationLiteral> getOcci_enumerationliterals() {
        return occi_enumerationliterals;
    }

    public void addOcci_enumerationliteral(Occi_enumerationliteral occi_enumerationliteral) {
        this.occi_enumerationliterals.add(occi_enumerationliteral);
    }
    public occi_EnumerationLiteral getOcci_enumerationliteral() {
        return occi_enumerationliteral;
    }

    public void setOcci_enumerationliteral(occi_EnumerationLiteral occi_enumerationliteral) {
        this.occi_enumerationliteral = occi_enumerationliteral;
    }

}