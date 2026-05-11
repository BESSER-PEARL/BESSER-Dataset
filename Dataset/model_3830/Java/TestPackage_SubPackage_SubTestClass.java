




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class TestPackage_SubPackage_SubTestClass  {

    private LocalDate testAttr;
    private String testStringAttr;
    private boolean testBooleanAttr;
    private String testRealAttr;
    private int testIntAttr;



    public TestPackage_SubPackage_SubTestClass(
        LocalDate testAttr,        String testStringAttr,        boolean testBooleanAttr,        String testRealAttr,        int testIntAttr    ) {
        this.testAttr = testAttr;
        this.testStringAttr = testStringAttr;
        this.testBooleanAttr = testBooleanAttr;
        this.testRealAttr = testRealAttr;
        this.testIntAttr = testIntAttr;
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
    public boolean getTestbooleanattr() {
        return testBooleanAttr;
    }

    public void setTestbooleanattr(boolean testBooleanAttr) {
        this.testBooleanAttr = testBooleanAttr;
    }
    public String getTestrealattr() {
        return testRealAttr;
    }

    public void setTestrealattr(String testRealAttr) {
        this.testRealAttr = testRealAttr;
    }
    public int getTestintattr() {
        return testIntAttr;
    }

    public void setTestintattr(int testIntAttr) {
        this.testIntAttr = testIntAttr;
    }


}