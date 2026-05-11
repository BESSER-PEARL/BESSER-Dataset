





import java.util.List;
import java.util.ArrayList;

public class uitf_UISUT extends Variable {

    private String objectURI;





    private uitf_TestCase uitf_testcase;


    public uitf_UISUT(
        String objectURI    ) {
        super(
        );
        this.objectURI = objectURI;
    }


    public String getObjecturi() {
        return objectURI;
    }

    public void setObjecturi(String objectURI) {
        this.objectURI = objectURI;
    }

    public uitf_TestCase getUitf_testcase() {
        return uitf_testcase;
    }

    public void setUitf_testcase(uitf_TestCase uitf_testcase) {
        this.uitf_testcase = uitf_testcase;
    }

}