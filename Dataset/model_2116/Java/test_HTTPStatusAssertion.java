





import java.util.List;
import java.util.ArrayList;

public class test_HTTPStatusAssertion extends Assertion {

    private String code;



    public test_HTTPStatusAssertion(
        String code    ) {
        super(
        );
        this.code = code;
    }


    public String getCode() {
        return code;
    }

    public void setCode(String code) {
        this.code = code;
    }


}