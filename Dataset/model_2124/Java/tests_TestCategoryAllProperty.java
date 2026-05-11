





import java.util.List;
import java.util.ArrayList;

public class tests_TestCategoryAllProperty extends DObject {

    private String testString;
    private float testFloat;
    private boolean testBool;
    private int testInt;
    private String testResource;
    private String testEnum;



    public tests_TestCategoryAllProperty(
        String testString,        float testFloat,        boolean testBool,        int testInt,        String testResource,        String testEnum    ) {
        super(
        );
        this.testString = testString;
        this.testFloat = testFloat;
        this.testBool = testBool;
        this.testInt = testInt;
        this.testResource = testResource;
        this.testEnum = testEnum;
    }


    public String getTeststring() {
        return testString;
    }

    public void setTeststring(String testString) {
        this.testString = testString;
    }
    public float getTestfloat() {
        return testFloat;
    }

    public void setTestfloat(float testFloat) {
        this.testFloat = testFloat;
    }
    public boolean getTestbool() {
        return testBool;
    }

    public void setTestbool(boolean testBool) {
        this.testBool = testBool;
    }
    public int getTestint() {
        return testInt;
    }

    public void setTestint(int testInt) {
        this.testInt = testInt;
    }
    public String getTestresource() {
        return testResource;
    }

    public void setTestresource(String testResource) {
        this.testResource = testResource;
    }
    public String getTestenum() {
        return testEnum;
    }

    public void setTestenum(String testEnum) {
        this.testEnum = testEnum;
    }


}