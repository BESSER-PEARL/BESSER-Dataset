





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Java_Field extends Class_Element {

    private String field_name;





    private tTCTest_Java_Class ttctest_java_class;


    public tTCTest_Java_Field(
        String field_name    ) {
        super(
        );
        this.field_name = field_name;
    }


    public String getField_name() {
        return field_name;
    }

    public void setField_name(String field_name) {
        this.field_name = field_name;
    }

    public tTCTest_Java_Class getTtctest_java_class() {
        return ttctest_java_class;
    }

    public void setTtctest_java_class(tTCTest_Java_Class ttctest_java_class) {
        this.ttctest_java_class = ttctest_java_class;
    }

}