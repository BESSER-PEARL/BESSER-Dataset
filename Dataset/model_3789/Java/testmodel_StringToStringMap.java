





import java.util.List;
import java.util.ArrayList;

public class testmodel_StringToStringMap  {

    private String value;
    private String key;





    private testmodel_TestElement testmodel_testelement;


    public testmodel_StringToStringMap(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public testmodel_TestElement getTestmodel_testelement() {
        return testmodel_testelement;
    }

    public void setTestmodel_testelement(testmodel_TestElement testmodel_testelement) {
        this.testmodel_testelement = testmodel_testelement;
    }

}