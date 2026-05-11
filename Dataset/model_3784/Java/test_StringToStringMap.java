





import java.util.List;
import java.util.ArrayList;

public class test_StringToStringMap  {

    private String key;
    private String value;





    private test_TestElement test_testelement;


    public test_StringToStringMap(
        String key,        String value    ) {
        this.key = key;
        this.value = value;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public test_TestElement getTest_testelement() {
        return test_testelement;
    }

    public void setTest_testelement(test_TestElement test_testelement) {
        this.test_testelement = test_testelement;
    }

}