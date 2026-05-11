





import java.util.List;
import java.util.ArrayList;

public class SecCon_Enumeration extends DataType {






    private List<SecCon_EnumerationLiteral> seccon_enumerationliterals;




    private SecCon_EnumerationLiteral seccon_enumerationliteral;


    public SecCon_Enumeration(
    ) {
        super(
        );
        this.seccon_enumerationliterals = new ArrayList<>();
    }

    public SecCon_Enumeration(
        ArrayList<SecCon_EnumerationLiteral> seccon_enumerationliterals    ) {
        this.seccon_enumerationliterals = seccon_enumerationliterals;
    }


    public List<SecCon_EnumerationLiteral> getSeccon_enumerationliterals() {
        return seccon_enumerationliterals;
    }

    public void addSeccon_enumerationliteral(Seccon_enumerationliteral seccon_enumerationliteral) {
        this.seccon_enumerationliterals.add(seccon_enumerationliteral);
    }
    public SecCon_EnumerationLiteral getSeccon_enumerationliteral() {
        return seccon_enumerationliteral;
    }

    public void setSeccon_enumerationliteral(SecCon_EnumerationLiteral seccon_enumerationliteral) {
        this.seccon_enumerationliteral = seccon_enumerationliteral;
    }

}