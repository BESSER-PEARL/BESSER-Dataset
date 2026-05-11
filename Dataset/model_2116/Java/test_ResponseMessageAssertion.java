





import java.util.List;
import java.util.ArrayList;

public class test_ResponseMessageAssertion extends Assertion {

    private String value;



    public test_ResponseMessageAssertion(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }


}