





import java.util.List;
import java.util.ArrayList;

public class TestPackage_TestClass  {

    private boolean testAttr;





    private SubTestClass subtestclass;


    public TestPackage_TestClass(
        boolean testAttr    ) {
        this.testAttr = testAttr;
    }


    public boolean getTestattr() {
        return testAttr;
    }

    public void setTestattr(boolean testAttr) {
        this.testAttr = testAttr;
    }

    public SubTestClass getSubtestclass() {
        return subtestclass;
    }

    public void setSubtestclass(SubTestClass subtestclass) {
        this.subtestclass = subtestclass;
    }

}