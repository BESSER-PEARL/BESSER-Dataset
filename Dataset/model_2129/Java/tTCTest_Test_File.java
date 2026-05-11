





import java.util.List;
import java.util.ArrayList;

public class tTCTest_Test_File  {

    private String name;





    private List<tTCTest_Refactoring_Instance> ttctest_refactoring_instances;




    private List<tTCTest_Java_Method> ttctest_java_methods;




    private List<tTCTest_Classes> ttctest_classess;


    public tTCTest_Test_File(
        String name    ) {
        this.name = name;
        this.ttctest_refactoring_instances = new ArrayList<>();
        this.ttctest_java_methods = new ArrayList<>();
        this.ttctest_classess = new ArrayList<>();
    }

    public tTCTest_Test_File(
        String name        ArrayList<tTCTest_Refactoring_Instance> ttctest_refactoring_instances,        ArrayList<tTCTest_Java_Method> ttctest_java_methods,        ArrayList<tTCTest_Classes> ttctest_classess    ) {
        this.name = name;
        this.ttctest_refactoring_instances = ttctest_refactoring_instances;
        this.ttctest_java_methods = ttctest_java_methods;
        this.ttctest_classess = ttctest_classess;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tTCTest_Refactoring_Instance> getTtctest_refactoring_instances() {
        return ttctest_refactoring_instances;
    }

    public void addTtctest_refactoring_instance(Ttctest_refactoring_instance ttctest_refactoring_instance) {
        this.ttctest_refactoring_instances.add(ttctest_refactoring_instance);
    }
    public List<tTCTest_Java_Method> getTtctest_java_methods() {
        return ttctest_java_methods;
    }

    public void addTtctest_java_method(Ttctest_java_method ttctest_java_method) {
        this.ttctest_java_methods.add(ttctest_java_method);
    }
    public List<tTCTest_Classes> getTtctest_classess() {
        return ttctest_classess;
    }

    public void addTtctest_classes(Ttctest_classes ttctest_classes) {
        this.ttctest_classess.add(ttctest_classes);
    }

}