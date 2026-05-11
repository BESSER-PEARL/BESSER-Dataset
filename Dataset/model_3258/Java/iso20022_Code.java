





import java.util.List;
import java.util.ArrayList;

public class iso20022_Code extends RepositoryConcept {

    private String codeName;





    private iso20022_CodeSet iso20022_codeset;




    private iso20022_CodeSet iso20022_codeset;


    public iso20022_Code(
        String codeName    ) {
        super(
        );
        this.codeName = codeName;
    }


    public String getCodename() {
        return codeName;
    }

    public void setCodename(String codeName) {
        this.codeName = codeName;
    }

    public iso20022_CodeSet getIso20022_codeset() {
        return iso20022_codeset;
    }

    public void setIso20022_codeset(iso20022_CodeSet iso20022_codeset) {
        this.iso20022_codeset = iso20022_codeset;
    }
    public iso20022_CodeSet getIso20022_codeset() {
        return iso20022_codeset;
    }

    public void setIso20022_codeset(iso20022_CodeSet iso20022_codeset) {
        this.iso20022_codeset = iso20022_codeset;
    }

}