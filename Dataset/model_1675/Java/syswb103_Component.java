





import java.util.List;
import java.util.ArrayList;

public class syswb103_Component extends NamedElement {






    private syswb103_System syswb103_system;




    private List<syswb103_Component> syswb103_components;




    private List<syswb103_Function> syswb103_functions;




    private syswb103_Function syswb103_function;




    private List<syswb103_Component> syswb103_components;


    public syswb103_Component(
    ) {
        super(
        );
        this.syswb103_components = new ArrayList<>();
        this.syswb103_functions = new ArrayList<>();
        this.syswb103_components = new ArrayList<>();
    }

    public syswb103_Component(
        ArrayList<syswb103_Component> syswb103_components,        ArrayList<syswb103_Function> syswb103_functions,        ArrayList<syswb103_Component> syswb103_components    ) {
        this.syswb103_components = syswb103_components;
        this.syswb103_functions = syswb103_functions;
        this.syswb103_components = syswb103_components;
    }


    public syswb103_System getSyswb103_system() {
        return syswb103_system;
    }

    public void setSyswb103_system(syswb103_System syswb103_system) {
        this.syswb103_system = syswb103_system;
    }
    public List<syswb103_Component> getSyswb103_components() {
        return syswb103_components;
    }

    public void addSyswb103_component(Syswb103_component syswb103_component) {
        this.syswb103_components.add(syswb103_component);
    }
    public List<syswb103_Function> getSyswb103_functions() {
        return syswb103_functions;
    }

    public void addSyswb103_function(Syswb103_function syswb103_function) {
        this.syswb103_functions.add(syswb103_function);
    }
    public syswb103_Function getSyswb103_function() {
        return syswb103_function;
    }

    public void setSyswb103_function(syswb103_Function syswb103_function) {
        this.syswb103_function = syswb103_function;
    }
    public List<syswb103_Component> getSyswb103_components() {
        return syswb103_components;
    }

    public void addSyswb103_component(Syswb103_component syswb103_component) {
        this.syswb103_components.add(syswb103_component);
    }

}