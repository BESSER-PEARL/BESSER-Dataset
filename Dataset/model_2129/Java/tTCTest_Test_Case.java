





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Test_Case  {

    private String java_program;
    private String description;
    private String name;





    private tTCTest_Test_File ttctest_test_file;


    public tTCTest_Test_Case(
        String java_program,        String description,        String name    ) {
        this.java_program = java_program;
        this.description = description;
        this.name = name;
    }


    public String getJava_program() {
        return java_program;
    }

    public void setJava_program(String java_program) {
        this.java_program = java_program;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tTCTest_Test_File getTtctest_test_file() {
        return ttctest_test_file;
    }

    public void setTtctest_test_file(tTCTest_Test_File ttctest_test_file) {
        this.ttctest_test_file = ttctest_test_file;
    }

}