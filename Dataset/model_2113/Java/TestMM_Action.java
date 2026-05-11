





import java.util.List;
import java.util.ArrayList;

public class TestMM_Action  {

    private String value;
    private String xpath;
    private String description;
    private String type;
    private String id;





    private TestMM_Test testmm_test;




    private TestMM_Test testmm_test;


    public TestMM_Action(
        String value,        String xpath,        String description,        String type,        String id    ) {
        this.value = value;
        this.xpath = xpath;
        this.description = description;
        this.type = type;
        this.id = id;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getXpath() {
        return xpath;
    }

    public void setXpath(String xpath) {
        this.xpath = xpath;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public TestMM_Test getTestmm_test() {
        return testmm_test;
    }

    public void setTestmm_test(TestMM_Test testmm_test) {
        this.testmm_test = testmm_test;
    }
    public TestMM_Test getTestmm_test() {
        return testmm_test;
    }

    public void setTestmm_test(TestMM_Test testmm_test) {
        this.testmm_test = testmm_test;
    }

}