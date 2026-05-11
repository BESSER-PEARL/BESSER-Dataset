





import java.util.List;
import java.util.ArrayList;

public class TestMM5_Action  {

    private String type;
    private String xpath;
    private String id;
    private String description;
    private String value;





    private TestMM5_Test testmm5_test;




    private TestMM5_Test testmm5_test;


    public TestMM5_Action(
        String type,        String xpath,        String id,        String description,        String value    ) {
        this.type = type;
        this.xpath = xpath;
        this.id = id;
        this.description = description;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getXpath() {
        return xpath;
    }

    public void setXpath(String xpath) {
        this.xpath = xpath;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public TestMM5_Test getTestmm5_test() {
        return testmm5_test;
    }

    public void setTestmm5_test(TestMM5_Test testmm5_test) {
        this.testmm5_test = testmm5_test;
    }
    public TestMM5_Test getTestmm5_test() {
        return testmm5_test;
    }

    public void setTestmm5_test(TestMM5_Test testmm5_test) {
        this.testmm5_test = testmm5_test;
    }

}