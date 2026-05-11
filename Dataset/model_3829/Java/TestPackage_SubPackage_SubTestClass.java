




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class TestPackage_SubPackage_SubTestClass  {

    private String testRealAttr;
    private String testStringAttr;
    private boolean testBooleanAttr;
    private LocalDate testAttr;
    private int testIntAttr;



    public TestPackage_SubPackage_SubTestClass(
        String testRealAttr,        String testStringAttr,        boolean testBooleanAttr,        LocalDate testAttr,        int testIntAttr    ) {
        this.testRealAttr = testRealAttr;
        this.testStringAttr = testStringAttr;
        this.testBooleanAttr = testBooleanAttr;
        this.testAttr = testAttr;
        this.testIntAttr = testIntAttr;
    }


    public String getTestrealattr() {
        return testRealAttr;
    }

    public void setTestrealattr(String testRealAttr) {
        this.testRealAttr = testRealAttr;
    }
    public String getTeststringattr() {
        return testStringAttr;
    }

    public void setTeststringattr(String testStringAttr) {
        this.testStringAttr = testStringAttr;
    }
    public boolean getTestbooleanattr() {
        return testBooleanAttr;
    }

    public void setTestbooleanattr(boolean testBooleanAttr) {
        this.testBooleanAttr = testBooleanAttr;
    }
    public LocalDate getTestattr() {
        return testAttr;
    }

    public void setTestattr(LocalDate testAttr) {
        this.testAttr = testAttr;
    }
    public int getTestintattr() {
        return testIntAttr;
    }

    public void setTestintattr(int testIntAttr) {
        this.testIntAttr = testIntAttr;
    }


}