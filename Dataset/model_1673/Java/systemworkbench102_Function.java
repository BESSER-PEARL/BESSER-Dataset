





import java.util.List;
import java.util.ArrayList;

public class systemworkbench102_Function extends Named {






    private systemworkbench102_Function systemworkbench102_function;




    private systemworkbench102_Component systemworkbench102_component;




    private systemworkbench102_System systemworkbench102_system;




    private systemworkbench102_Function systemworkbench102_function;




    private List<systemworkbench102_FunctionProperty> systemworkbench102_functionpropertys;




    private systemworkbench102_Component systemworkbench102_component;


    public systemworkbench102_Function(
    ) {
        super(
        );
        this.systemworkbench102_functionpropertys = new ArrayList<>();
    }

    public systemworkbench102_Function(
        ArrayList<systemworkbench102_FunctionProperty> systemworkbench102_functionpropertys    ) {
        this.systemworkbench102_functionpropertys = systemworkbench102_functionpropertys;
    }


    public systemworkbench102_Function getSystemworkbench102_function() {
        return systemworkbench102_function;
    }

    public void setSystemworkbench102_function(systemworkbench102_Function systemworkbench102_function) {
        this.systemworkbench102_function = systemworkbench102_function;
    }
    public systemworkbench102_Component getSystemworkbench102_component() {
        return systemworkbench102_component;
    }

    public void setSystemworkbench102_component(systemworkbench102_Component systemworkbench102_component) {
        this.systemworkbench102_component = systemworkbench102_component;
    }
    public systemworkbench102_System getSystemworkbench102_system() {
        return systemworkbench102_system;
    }

    public void setSystemworkbench102_system(systemworkbench102_System systemworkbench102_system) {
        this.systemworkbench102_system = systemworkbench102_system;
    }
    public systemworkbench102_Function getSystemworkbench102_function() {
        return systemworkbench102_function;
    }

    public void setSystemworkbench102_function(systemworkbench102_Function systemworkbench102_function) {
        this.systemworkbench102_function = systemworkbench102_function;
    }
    public List<systemworkbench102_FunctionProperty> getSystemworkbench102_functionpropertys() {
        return systemworkbench102_functionpropertys;
    }

    public void addSystemworkbench102_functionproperty(Systemworkbench102_functionproperty systemworkbench102_functionproperty) {
        this.systemworkbench102_functionpropertys.add(systemworkbench102_functionproperty);
    }
    public systemworkbench102_Component getSystemworkbench102_component() {
        return systemworkbench102_component;
    }

    public void setSystemworkbench102_component(systemworkbench102_Component systemworkbench102_component) {
        this.systemworkbench102_component = systemworkbench102_component;
    }

}