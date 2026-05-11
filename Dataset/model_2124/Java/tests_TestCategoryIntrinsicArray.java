





import java.util.List;
import java.util.ArrayList;

public class tests_TestCategoryIntrinsicArray extends DObject {

    private String testStringArrayStatic;
    private String testStringArrayDynamic;



    public tests_TestCategoryIntrinsicArray(
        String testStringArrayStatic,        String testStringArrayDynamic    ) {
        super(
        );
        this.testStringArrayStatic = testStringArrayStatic;
        this.testStringArrayDynamic = testStringArrayDynamic;
    }


    public String getTeststringarraystatic() {
        return testStringArrayStatic;
    }

    public void setTeststringarraystatic(String testStringArrayStatic) {
        this.testStringArrayStatic = testStringArrayStatic;
    }
    public String getTeststringarraydynamic() {
        return testStringArrayDynamic;
    }

    public void setTeststringarraydynamic(String testStringArrayDynamic) {
        this.testStringArrayDynamic = testStringArrayDynamic;
    }


}