





import java.util.List;
import java.util.ArrayList;

public class myDsl_Verb extends Member {

    private String verb;
    private String qa;



    public myDsl_Verb(
        String verb,        String qa    ) {
        super(
        );
        this.verb = verb;
        this.qa = qa;
    }


    public String getVerb() {
        return verb;
    }

    public void setVerb(String verb) {
        this.verb = verb;
    }
    public String getQa() {
        return qa;
    }

    public void setQa(String qa) {
        this.qa = qa;
    }


}