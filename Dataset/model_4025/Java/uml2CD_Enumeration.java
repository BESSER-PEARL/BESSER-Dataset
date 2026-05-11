





import java.util.List;
import java.util.ArrayList;

public class uml2CD_Enumeration extends DataType {






    private List<uml2CD_EnumerationLiteral> uml2cd_enumerationliterals;




    private uml2CD_EnumerationLiteral uml2cd_enumerationliteral;


    public uml2CD_Enumeration(
    ) {
        super(
        );
        this.uml2cd_enumerationliterals = new ArrayList<>();
    }

    public uml2CD_Enumeration(
        ArrayList<uml2CD_EnumerationLiteral> uml2cd_enumerationliterals    ) {
        this.uml2cd_enumerationliterals = uml2cd_enumerationliterals;
    }


    public List<uml2CD_EnumerationLiteral> getUml2cd_enumerationliterals() {
        return uml2cd_enumerationliterals;
    }

    public void addUml2cd_enumerationliteral(Uml2cd_enumerationliteral uml2cd_enumerationliteral) {
        this.uml2cd_enumerationliterals.add(uml2cd_enumerationliteral);
    }
    public uml2CD_EnumerationLiteral getUml2cd_enumerationliteral() {
        return uml2cd_enumerationliteral;
    }

    public void setUml2cd_enumerationliteral(uml2CD_EnumerationLiteral uml2cd_enumerationliteral) {
        this.uml2cd_enumerationliteral = uml2cd_enumerationliteral;
    }

}