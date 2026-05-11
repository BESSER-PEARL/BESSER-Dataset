





import java.util.List;
import java.util.ArrayList;

public class TestPackage_TestClass1 extends AbstractTestClass {

    private String theAttributeToListen;



    public TestPackage_TestClass1(
        String theAttributeToListen    ) {
        super(
        );
        this.theAttributeToListen = theAttributeToListen;
    }


    public String getTheattributetolisten() {
        return theAttributeToListen;
    }

    public void setTheattributetolisten(String theAttributeToListen) {
        this.theAttributeToListen = theAttributeToListen;
    }


}