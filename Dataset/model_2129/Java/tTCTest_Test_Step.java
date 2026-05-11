





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Test_Step extends Test_Step_Element {






    private List<tTCTest_Test_Step_Element> ttctest_test_step_elements;


    public tTCTest_Test_Step(
    ) {
        super(
        );
        this.ttctest_test_step_elements = new ArrayList<>();
    }

    public tTCTest_Test_Step(
        ArrayList<tTCTest_Test_Step_Element> ttctest_test_step_elements    ) {
        this.ttctest_test_step_elements = ttctest_test_step_elements;
    }


    public List<tTCTest_Test_Step_Element> getTtctest_test_step_elements() {
        return ttctest_test_step_elements;
    }

    public void addTtctest_test_step_element(Ttctest_test_step_element ttctest_test_step_element) {
        this.ttctest_test_step_elements.add(ttctest_test_step_element);
    }

}