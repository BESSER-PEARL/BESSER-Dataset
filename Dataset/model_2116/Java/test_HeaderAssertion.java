





import java.util.List;
import java.util.ArrayList;

public class test_HeaderAssertion extends Assertion {

    private String key;



    public test_HeaderAssertion(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}