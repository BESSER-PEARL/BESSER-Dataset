





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Methods  {

    private String name;





    private List<tTCTest_Java_Method> ttctest_java_methods;


    public tTCTest_Methods(
        String name    ) {
        this.name = name;
        this.ttctest_java_methods = new ArrayList<>();
    }

    public tTCTest_Methods(
        String name        ArrayList<tTCTest_Java_Method> ttctest_java_methods    ) {
        this.name = name;
        this.ttctest_java_methods = ttctest_java_methods;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tTCTest_Java_Method> getTtctest_java_methods() {
        return ttctest_java_methods;
    }

    public void addTtctest_java_method(Ttctest_java_method ttctest_java_method) {
        this.ttctest_java_methods.add(ttctest_java_method);
    }

}