





import java.util.List;
import java.util.ArrayList;

public class test_Contact  {

    private String type;
    private String value;





    private test_Person test_person;


    public test_Contact(
        String type,        String value    ) {
        this.type = type;
        this.value = value;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public test_Person getTest_person() {
        return test_person;
    }

    public void setTest_person(test_Person test_person) {
        this.test_person = test_person;
    }

}