





import java.util.List;
import java.util.ArrayList;

public class ansic_enumeration_constant  {

    private String identifier;





    private ansic_enumerator ansic_enumerator;


    public ansic_enumeration_constant(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public ansic_enumerator getAnsic_enumerator() {
        return ansic_enumerator;
    }

    public void setAnsic_enumerator(ansic_enumerator ansic_enumerator) {
        this.ansic_enumerator = ansic_enumerator;
    }

}