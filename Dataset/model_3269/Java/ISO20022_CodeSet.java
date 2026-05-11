





import java.util.List;
import java.util.ArrayList;

public class ISO20022_CodeSet extends XSDString {

    private String identificationScheme;





    private ISO20022_CodeSet iso20022_codeset;




    private List<ISO20022_Code> iso20022_codes;




    private List<ISO20022_CodeSet> iso20022_codesets;




    private ISO20022_Code iso20022_code;


    public ISO20022_CodeSet(
        String identificationScheme    ) {
        super(
        );
        this.identificationScheme = identificationScheme;
        this.iso20022_codes = new ArrayList<>();
        this.iso20022_codesets = new ArrayList<>();
    }

    public ISO20022_CodeSet(
        String identificationScheme        ArrayList<ISO20022_Code> iso20022_codes,        ArrayList<ISO20022_CodeSet> iso20022_codesets    ) {
        this.identificationScheme = identificationScheme;
        this.iso20022_codes = iso20022_codes;
        this.iso20022_codesets = iso20022_codesets;
    }

    public String getIdentificationscheme() {
        return identificationScheme;
    }

    public void setIdentificationscheme(String identificationScheme) {
        this.identificationScheme = identificationScheme;
    }

    public ISO20022_CodeSet getIso20022_codeset() {
        return iso20022_codeset;
    }

    public void setIso20022_codeset(ISO20022_CodeSet iso20022_codeset) {
        this.iso20022_codeset = iso20022_codeset;
    }
    public List<ISO20022_Code> getIso20022_codes() {
        return iso20022_codes;
    }

    public void addIso20022_code(Iso20022_code iso20022_code) {
        this.iso20022_codes.add(iso20022_code);
    }
    public List<ISO20022_CodeSet> getIso20022_codesets() {
        return iso20022_codesets;
    }

    public void addIso20022_codeset(Iso20022_codeset iso20022_codeset) {
        this.iso20022_codesets.add(iso20022_codeset);
    }
    public ISO20022_Code getIso20022_code() {
        return iso20022_code;
    }

    public void setIso20022_code(ISO20022_Code iso20022_code) {
        this.iso20022_code = iso20022_code;
    }

}