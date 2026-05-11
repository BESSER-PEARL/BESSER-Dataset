




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class TestPackage_SubPackage_SubTestClass  {

    private LocalDate testAttr;
    private String testStringAttr;
    private int testIntAttr;
    private String testRealAttr;
    private boolean testBooleanAttr;



    public TestPackage_SubPackage_SubTestClass(
        LocalDate testAttr,        String testStringAttr,        int testIntAttr,        String testRealAttr,        boolean testBooleanAttr    ) {
        this.testAttr = testAttr;
        this.testStringAttr = testStringAttr;
        this.testIntAttr = testIntAttr;
        this.testRealAttr = testRealAttr;
        this.testBooleanAttr = testBooleanAttr;
    }


    public LocalDate getTestattr() {
        return testAttr;
    }

    public void setTestattr(LocalDate testAttr) {
        this.testAttr = testAttr;
    }
    public String getTeststringattr() {
        return testStringAttr;
    }

    public void setTeststringattr(String testStringAttr) {
        this.testStringAttr = testStringAttr;
    }
    public int getTestintattr() {
        return testIntAttr;
    }

    public void setTestintattr(int testIntAttr) {
        this.testIntAttr = testIntAttr;
    }
    public String getTestrealattr() {
        return testRealAttr;
    }

    public void setTestrealattr(String testRealAttr) {
        this.testRealAttr = testRealAttr;
    }
    public boolean getTestbooleanattr() {
        return testBooleanAttr;
    }

    public void setTestbooleanattr(boolean testBooleanAttr) {
        this.testBooleanAttr = testBooleanAttr;
    }


}