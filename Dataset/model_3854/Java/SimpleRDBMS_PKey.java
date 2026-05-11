





import java.util.List;
import java.util.ArrayList;

public class SimpleRDBMS_PKey extends FKey {

    private String test;



    public SimpleRDBMS_PKey(
        String test    ) {
        super(
        );
        this.test = test;
    }


    public String getTest() {
        return test;
    }

    public void setTest(String test) {
        this.test = test;
    }


}