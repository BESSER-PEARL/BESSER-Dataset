





import java.util.List;
import java.util.ArrayList;

public class testall_Interface  {

    private String name;
    private String signature;





    private testall_Binding testall_binding;




    private List<testall_Binding> testall_bindings;




    private testall_Binding testall_binding;


    public testall_Interface(
        String name,        String signature    ) {
        this.name = name;
        this.signature = signature;
        this.testall_bindings = new ArrayList<>();
    }

    public testall_Interface(
        String name,        String signature        ArrayList<testall_Binding> testall_bindings    ) {
        this.name = name;
        this.signature = signature;
        this.testall_bindings = testall_bindings;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getSignature() {
        return signature;
    }

    public void setSignature(String signature) {
        this.signature = signature;
    }

    public testall_Binding getTestall_binding() {
        return testall_binding;
    }

    public void setTestall_binding(testall_Binding testall_binding) {
        this.testall_binding = testall_binding;
    }
    public List<testall_Binding> getTestall_bindings() {
        return testall_bindings;
    }

    public void addTestall_binding(Testall_binding testall_binding) {
        this.testall_bindings.add(testall_binding);
    }
    public testall_Binding getTestall_binding() {
        return testall_binding;
    }

    public void setTestall_binding(testall_Binding testall_binding) {
        this.testall_binding = testall_binding;
    }

}