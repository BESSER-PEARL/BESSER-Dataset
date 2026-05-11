





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Warning  {

    private String message;





    private tTCTest_Condition ttctest_condition;


    public tTCTest_Warning(
        String message    ) {
        this.message = message;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }

    public tTCTest_Condition getTtctest_condition() {
        return ttctest_condition;
    }

    public void setTtctest_condition(tTCTest_Condition ttctest_condition) {
        this.ttctest_condition = ttctest_condition;
    }

}