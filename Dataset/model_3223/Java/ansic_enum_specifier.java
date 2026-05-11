





import java.util.List;
import java.util.ArrayList;

public class ansic_enum_specifier  {

    private String identifier;





    private ansic_type_specifier ansic_type_specifier;


    public ansic_enum_specifier(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public ansic_type_specifier getAnsic_type_specifier() {
        return ansic_type_specifier;
    }

    public void setAnsic_type_specifier(ansic_type_specifier ansic_type_specifier) {
        this.ansic_type_specifier = ansic_type_specifier;
    }

}