





import java.util.List;
import java.util.ArrayList;

public class test_Parameter  {

    private String location;
    private String value;
    private String name;





    private test_APIRequest test_apirequest;


    public test_Parameter(
        String location,        String value,        String name    ) {
        this.location = location;
        this.value = value;
        this.name = name;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public test_APIRequest getTest_apirequest() {
        return test_apirequest;
    }

    public void setTest_apirequest(test_APIRequest test_apirequest) {
        this.test_apirequest = test_apirequest;
    }

}