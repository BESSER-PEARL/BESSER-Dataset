





import java.util.List;
import java.util.ArrayList;

public class test_Assertion  {

    private String errorMessage;





    private test_APIRequest test_apirequest;


    public test_Assertion(
        String errorMessage    ) {
        this.errorMessage = errorMessage;
    }


    public String getErrormessage() {
        return errorMessage;
    }

    public void setErrormessage(String errorMessage) {
        this.errorMessage = errorMessage;
    }

    public test_APIRequest getTest_apirequest() {
        return test_apirequest;
    }

    public void setTest_apirequest(test_APIRequest test_apirequest) {
        this.test_apirequest = test_apirequest;
    }

}