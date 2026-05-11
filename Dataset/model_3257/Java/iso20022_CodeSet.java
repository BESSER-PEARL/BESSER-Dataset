





import java.util.List;
import java.util.ArrayList;

public class iso20022_CodeSet extends String {

    private String identificationScheme;





    private iso20022_CodeSet iso20022_codeset;




    private List<iso20022_Code> iso20022_codes;




    private iso20022_CodeSet iso20022_codeset;




    private iso20022_Code iso20022_code;


    public iso20022_CodeSet(
        String identificationScheme    ) {
        super(
        );
        this.identificationScheme = identificationScheme;
        this.iso20022_codes = new ArrayList<>();
    }

    public iso20022_CodeSet(
        String identificationScheme        ArrayList<iso20022_Code> iso20022_codes    ) {
        this.identificationScheme = identificationScheme;
        this.iso20022_codes = iso20022_codes;
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
    public List<iso20022_Code> getIso20022_codes() {
        return iso20022_codes;
    }

    public void addIso20022_code(Iso20022_code iso20022_code) {
        this.iso20022_codes.add(iso20022_code);
    }
    public iso20022_CodeSet getIso20022_codeset() {
        return iso20022_codeset;
    }

    public void setIso20022_codeset(iso20022_CodeSet iso20022_codeset) {
        this.iso20022_codeset = iso20022_codeset;
    }
    public iso20022_Code getIso20022_code() {
        return iso20022_code;
    }

    public void setIso20022_code(iso20022_Code iso20022_code) {
        this.iso20022_code = iso20022_code;
    }

}