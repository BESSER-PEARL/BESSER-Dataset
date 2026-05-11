





import java.util.List;
import java.util.ArrayList;

public class gDSL_PAT  {

    private String bitpat;
    private String id;
    private String int;
    private String uscore;





    private gDSL_PAT gdsl_pat;




    private gDSL_CaseExp gdsl_caseexp;


    public gDSL_PAT(
        String bitpat,        String id,        String int,        String uscore    ) {
        this.bitpat = bitpat;
        this.id = id;
        this.int = int;
        this.uscore = uscore;
    }


    public String getBitpat() {
        return bitpat;
    }

    public void setBitpat(String bitpat) {
        this.bitpat = bitpat;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getInt() {
        return int;
    }

    public void setInt(String int) {
        this.int = int;
    }
    public String getUscore() {
        return uscore;
    }

    public void setUscore(String uscore) {
        this.uscore = uscore;
    }

    public gDSL_PAT getGdsl_pat() {
        return gdsl_pat;
    }

    public void setGdsl_pat(gDSL_PAT gdsl_pat) {
        this.gdsl_pat = gdsl_pat;
    }
    public gDSL_CaseExp getGdsl_caseexp() {
        return gdsl_caseexp;
    }

    public void setGdsl_caseexp(gDSL_CaseExp gdsl_caseexp) {
        this.gdsl_caseexp = gdsl_caseexp;
    }

}