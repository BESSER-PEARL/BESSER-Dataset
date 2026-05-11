





import java.util.List;
import java.util.ArrayList;

public class ISO20022_IdentifierSet extends XSDString {

    private String identificationScheme;



    public ISO20022_IdentifierSet(
        String identificationScheme    ) {
        super(
        );
        this.identificationScheme = identificationScheme;
    }


    public String getIdentificationscheme() {
        return identificationScheme;
    }

    public void setIdentificationscheme(String identificationScheme) {
        this.identificationScheme = identificationScheme;
    }


}