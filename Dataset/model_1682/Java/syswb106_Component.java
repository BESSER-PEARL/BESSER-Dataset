





import java.util.List;
import java.util.ArrayList;

public class syswb106_Component  {






    private List<syswb106_Component> syswb106_components;




    private syswb106_System syswb106_system;




    private List<syswb106_Component> syswb106_components;




    private syswb106_Function syswb106_function;




    private List<syswb106_Function> syswb106_functions;


    public syswb106_Component(
    ) {
        this.syswb106_components = new ArrayList<>();
        this.syswb106_components = new ArrayList<>();
        this.syswb106_functions = new ArrayList<>();
    }

    public syswb106_Component(
        ArrayList<syswb106_Component> syswb106_components,        ArrayList<syswb106_Component> syswb106_components,        ArrayList<syswb106_Function> syswb106_functions    ) {
        this.syswb106_components = syswb106_components;
        this.syswb106_components = syswb106_components;
        this.syswb106_functions = syswb106_functions;
    }


    public List<syswb106_Component> getSyswb106_components() {
        return syswb106_components;
    }

    public void addSyswb106_component(Syswb106_component syswb106_component) {
        this.syswb106_components.add(syswb106_component);
    }
    public syswb106_System getSyswb106_system() {
        return syswb106_system;
    }

    public void setSyswb106_system(syswb106_System syswb106_system) {
        this.syswb106_system = syswb106_system;
    }
    public List<syswb106_Component> getSyswb106_components() {
        return syswb106_components;
    }

    public void addSyswb106_component(Syswb106_component syswb106_component) {
        this.syswb106_components.add(syswb106_component);
    }
    public syswb106_Function getSyswb106_function() {
        return syswb106_function;
    }

    public void setSyswb106_function(syswb106_Function syswb106_function) {
        this.syswb106_function = syswb106_function;
    }
    public List<syswb106_Function> getSyswb106_functions() {
        return syswb106_functions;
    }

    public void addSyswb106_function(Syswb106_function syswb106_function) {
        this.syswb106_functions.add(syswb106_function);
    }

}