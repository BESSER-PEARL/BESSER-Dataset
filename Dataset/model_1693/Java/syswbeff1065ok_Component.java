





import java.util.List;
import java.util.ArrayList;

public class syswbeff1065ok_Component  {

    private String name;





    private syswbeff1065ok_Function syswbeff1065ok_function;




    private List<syswbeff1065ok_Function> syswbeff1065ok_functions;




    private syswbeff1065ok_Component syswbeff1065ok_component;




    private syswbeff1065ok_Component syswbeff1065ok_component;


    public syswbeff1065ok_Component(
        String name    ) {
        this.name = name;
        this.syswbeff1065ok_functions = new ArrayList<>();
    }

    public syswbeff1065ok_Component(
        String name        ArrayList<syswbeff1065ok_Function> syswbeff1065ok_functions    ) {
        this.name = name;
        this.syswbeff1065ok_functions = syswbeff1065ok_functions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public syswbeff1065ok_Function getSyswbeff1065ok_function() {
        return syswbeff1065ok_function;
    }

    public void setSyswbeff1065ok_function(syswbeff1065ok_Function syswbeff1065ok_function) {
        this.syswbeff1065ok_function = syswbeff1065ok_function;
    }
    public List<syswbeff1065ok_Function> getSyswbeff1065ok_functions() {
        return syswbeff1065ok_functions;
    }

    public void addSyswbeff1065ok_function(Syswbeff1065ok_function syswbeff1065ok_function) {
        this.syswbeff1065ok_functions.add(syswbeff1065ok_function);
    }
    public syswbeff1065ok_Component getSyswbeff1065ok_component() {
        return syswbeff1065ok_component;
    }

    public void setSyswbeff1065ok_component(syswbeff1065ok_Component syswbeff1065ok_component) {
        this.syswbeff1065ok_component = syswbeff1065ok_component;
    }
    public syswbeff1065ok_Component getSyswbeff1065ok_component() {
        return syswbeff1065ok_component;
    }

    public void setSyswbeff1065ok_component(syswbeff1065ok_Component syswbeff1065ok_component) {
        this.syswbeff1065ok_component = syswbeff1065ok_component;
    }

}