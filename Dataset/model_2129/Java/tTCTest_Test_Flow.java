





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Test_Flow  {






    private List<tTCTest_Test_Step_Element> ttctest_test_step_elements;




    private tTCTest_Test_Case ttctest_test_case;


    public tTCTest_Test_Flow(
    ) {
        this.ttctest_test_step_elements = new ArrayList<>();
    }

    public tTCTest_Test_Flow(
        ArrayList<tTCTest_Test_Step_Element> ttctest_test_step_elements    ) {
        this.ttctest_test_step_elements = ttctest_test_step_elements;
    }


    public List<tTCTest_Test_Step_Element> getTtctest_test_step_elements() {
        return ttctest_test_step_elements;
    }

    public void addTtctest_test_step_element(Ttctest_test_step_element ttctest_test_step_element) {
        this.ttctest_test_step_elements.add(ttctest_test_step_element);
    }
    public tTCTest_Test_Case getTtctest_test_case() {
        return ttctest_test_case;
    }

    public void setTtctest_test_case(tTCTest_Test_Case ttctest_test_case) {
        this.ttctest_test_case = ttctest_test_case;
    }

}