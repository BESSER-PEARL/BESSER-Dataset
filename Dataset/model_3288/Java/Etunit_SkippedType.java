





import java.util.List;
import java.util.ArrayList;

public class Etunit_SkippedType  {

    private String message;
    private String mixed;





    private Etunit_TestcaseType etunit_testcasetype;




    private Etunit_DocumentRoot etunit_documentroot;


    public Etunit_SkippedType(
        String message,        String mixed    ) {
        this.message = message;
        this.mixed = mixed;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public Etunit_TestcaseType getEtunit_testcasetype() {
        return etunit_testcasetype;
    }

    public void setEtunit_testcasetype(Etunit_TestcaseType etunit_testcasetype) {
        this.etunit_testcasetype = etunit_testcasetype;
    }
    public Etunit_DocumentRoot getEtunit_documentroot() {
        return etunit_documentroot;
    }

    public void setEtunit_documentroot(Etunit_DocumentRoot etunit_documentroot) {
        this.etunit_documentroot = etunit_documentroot;
    }

}