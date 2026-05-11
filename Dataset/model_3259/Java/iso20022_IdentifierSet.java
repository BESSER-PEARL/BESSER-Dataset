





import java.util.List;
import java.util.ArrayList;

public class iso20022_IdentifierSet extends String {

    private String identificationScheme;



    public iso20022_IdentifierSet(
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