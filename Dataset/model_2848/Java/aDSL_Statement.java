





import java.util.List;
import java.util.ArrayList;

public class aDSL_Statement  {






    private aDSL_Body adsl_body;




    private aDSL_WhenStatement adsl_whenstatement;




    private aDSL_AtomicStatement adsl_atomicstatement;


    public aDSL_Statement(
    ) {
    }



    public aDSL_Body getAdsl_body() {
        return adsl_body;
    }

    public void setAdsl_body(aDSL_Body adsl_body) {
        this.adsl_body = adsl_body;
    }
    public aDSL_WhenStatement getAdsl_whenstatement() {
        return adsl_whenstatement;
    }

    public void setAdsl_whenstatement(aDSL_WhenStatement adsl_whenstatement) {
        this.adsl_whenstatement = adsl_whenstatement;
    }
    public aDSL_AtomicStatement getAdsl_atomicstatement() {
        return adsl_atomicstatement;
    }

    public void setAdsl_atomicstatement(aDSL_AtomicStatement adsl_atomicstatement) {
        this.adsl_atomicstatement = adsl_atomicstatement;
    }

}