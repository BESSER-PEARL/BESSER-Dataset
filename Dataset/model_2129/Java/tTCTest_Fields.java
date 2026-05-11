





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Fields  {

    private String name;





    private List<tTCTest_Java_Field> ttctest_java_fields;


    public tTCTest_Fields(
        String name    ) {
        this.name = name;
        this.ttctest_java_fields = new ArrayList<>();
    }

    public tTCTest_Fields(
        String name        ArrayList<tTCTest_Java_Field> ttctest_java_fields    ) {
        this.name = name;
        this.ttctest_java_fields = ttctest_java_fields;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tTCTest_Java_Field> getTtctest_java_fields() {
        return ttctest_java_fields;
    }

    public void addTtctest_java_field(Ttctest_java_field ttctest_java_field) {
        this.ttctest_java_fields.add(ttctest_java_field);
    }

}