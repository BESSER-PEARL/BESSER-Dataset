





import java.util.List;
import java.util.ArrayList;

public class iso20022_CodeSet extends String {

    private String identificationScheme;





    private iso20022_CodeSet iso20022_codeset;




    private List<iso20022_CodeSet> iso20022_codesets;


    public iso20022_CodeSet(
        String identificationScheme    ) {
        super(
        );
        this.identificationScheme = identificationScheme;
        this.iso20022_codesets = new ArrayList<>();
    }

    public iso20022_CodeSet(
        String identificationScheme        ArrayList<iso20022_CodeSet> iso20022_codesets    ) {
        this.identificationScheme = identificationScheme;
        this.iso20022_codesets = iso20022_codesets;
    }

    public String getIdentificationscheme() {
        return identificationScheme;
    }

    public void setIdentificationscheme(String identificationScheme) {
        this.identificationScheme = identificationScheme;
    }

    public iso20022_CodeSet getIso20022_codeset() {
        return iso20022_codeset;
    }

    public void setIso20022_codeset(iso20022_CodeSet iso20022_codeset) {
        this.iso20022_codeset = iso20022_codeset;
    }
    public List<iso20022_CodeSet> getIso20022_codesets() {
        return iso20022_codesets;
    }

    public void addIso20022_codeset(Iso20022_codeset iso20022_codeset) {
        this.iso20022_codesets.add(iso20022_codeset);
    }

}