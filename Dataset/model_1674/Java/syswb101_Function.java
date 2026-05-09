





import java.util.List;
import java.util.ArrayList;

public class syswb101_Function extends Named {






    private syswb101_System syswb101_system;




    private syswb101_Component syswb101_component;




    private syswb101_Function syswb101_function;




    private List<syswb101_Function> syswb101_functions;




    private syswb101_Component syswb101_component;


    public syswb101_Function(
    ) {
        super(
        );
        this.syswb101_functions = new ArrayList<>();
    }

    public syswb101_Function(
        ArrayList<syswb101_Function> syswb101_functions    ) {
        this.syswb101_functions = syswb101_functions;
    }


    public syswb101_System getSyswb101_system() {
        return syswb101_system;
    }

    public void setSyswb101_system(syswb101_System syswb101_system) {
        this.syswb101_system = syswb101_system;
    }
    public syswb101_Component getSyswb101_component() {
        return syswb101_component;
    }

    public void setSyswb101_component(syswb101_Component syswb101_component) {
        this.syswb101_component = syswb101_component;
    }
    public syswb101_Function getSyswb101_function() {
        return syswb101_function;
    }

    public void setSyswb101_function(syswb101_Function syswb101_function) {
        this.syswb101_function = syswb101_function;
    }
    public List<syswb101_Function> getSyswb101_functions() {
        return syswb101_functions;
    }

    public void addSyswb101_function(Syswb101_function syswb101_function) {
        this.syswb101_functions.add(syswb101_function);
    }
    public syswb101_Component getSyswb101_component() {
        return syswb101_component;
    }

    public void setSyswb101_component(syswb101_Component syswb101_component) {
        this.syswb101_component = syswb101_component;
    }

}