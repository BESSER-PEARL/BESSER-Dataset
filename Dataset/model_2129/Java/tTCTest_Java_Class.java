





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Java_Class  {

    private String package;
    private String name;
    private String class_name;





    private tTCTest_Test_File ttctest_test_file;




    private tTCTest_Classes ttctest_classes;




    private tTCTest_Java_Method ttctest_java_method;


    public tTCTest_Java_Class(
        String package,        String name,        String class_name    ) {
        this.package = package;
        this.name = name;
        this.class_name = class_name;
    }


    public String getPackage() {
        return package;
    }

    public void setPackage(String package) {
        this.package = package;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getClass_name() {
        return class_name;
    }

    public void setClass_name(String class_name) {
        this.class_name = class_name;
    }

    public tTCTest_Test_File getTtctest_test_file() {
        return ttctest_test_file;
    }

    public void setTtctest_test_file(tTCTest_Test_File ttctest_test_file) {
        this.ttctest_test_file = ttctest_test_file;
    }
    public tTCTest_Classes getTtctest_classes() {
        return ttctest_classes;
    }

    public void setTtctest_classes(tTCTest_Classes ttctest_classes) {
        this.ttctest_classes = ttctest_classes;
    }
    public tTCTest_Java_Method getTtctest_java_method() {
        return ttctest_java_method;
    }

    public void setTtctest_java_method(tTCTest_Java_Method ttctest_java_method) {
        this.ttctest_java_method = ttctest_java_method;
    }

}