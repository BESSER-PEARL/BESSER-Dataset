





import java.util.List;
import java.util.ArrayList;

public class syswbeff106_Component  {

    private String name;





    private List<syswbeff106_Function> syswbeff106_functions;




    private List<syswbeff106_Component> syswbeff106_components;




    private List<syswbeff106_Component> syswbeff106_components;




    private syswbeff106_Function syswbeff106_function;


    public syswbeff106_Component(
        String name    ) {
        this.name = name;
        this.syswbeff106_functions = new ArrayList<>();
        this.syswbeff106_components = new ArrayList<>();
        this.syswbeff106_components = new ArrayList<>();
    }

    public syswbeff106_Component(
        String name        ArrayList<syswbeff106_Function> syswbeff106_functions,        ArrayList<syswbeff106_Component> syswbeff106_components,        ArrayList<syswbeff106_Component> syswbeff106_components    ) {
        this.name = name;
        this.syswbeff106_functions = syswbeff106_functions;
        this.syswbeff106_components = syswbeff106_components;
        this.syswbeff106_components = syswbeff106_components;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<syswbeff106_Function> getSyswbeff106_functions() {
        return syswbeff106_functions;
    }

    public void addSyswbeff106_function(Syswbeff106_function syswbeff106_function) {
        this.syswbeff106_functions.add(syswbeff106_function);
    }
    public List<syswbeff106_Component> getSyswbeff106_components() {
        return syswbeff106_components;
    }

    public void addSyswbeff106_component(Syswbeff106_component syswbeff106_component) {
        this.syswbeff106_components.add(syswbeff106_component);
    }
    public List<syswbeff106_Component> getSyswbeff106_components() {
        return syswbeff106_components;
    }

    public void addSyswbeff106_component(Syswbeff106_component syswbeff106_component) {
        this.syswbeff106_components.add(syswbeff106_component);
    }
    public syswbeff106_Function getSyswbeff106_function() {
        return syswbeff106_function;
    }

    public void setSyswbeff106_function(syswbeff106_Function syswbeff106_function) {
        this.syswbeff106_function = syswbeff106_function;
    }

}