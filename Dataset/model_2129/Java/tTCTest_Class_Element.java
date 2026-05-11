





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Class_Element  {

    private String name;





    private tTCTest_Containment ttctest_containment;


    public tTCTest_Class_Element(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tTCTest_Containment getTtctest_containment() {
        return ttctest_containment;
    }

    public void setTtctest_containment(tTCTest_Containment ttctest_containment) {
        this.ttctest_containment = ttctest_containment;
    }

}