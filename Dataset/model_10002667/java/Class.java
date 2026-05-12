





import java.util.List;
import java.util.ArrayList;

public class Class  {

    private String attribute;
    private String test;



    public Class(
        String attribute,        String test    ) {
        this.attribute = attribute;
        this.test = test;
    }


    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getTest() {
        return test;
    }

    public void setTest(String test) {
        this.test = test;
    }


}