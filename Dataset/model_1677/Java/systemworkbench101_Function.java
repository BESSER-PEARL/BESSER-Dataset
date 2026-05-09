





import java.util.List;
import java.util.ArrayList;

public class systemworkbench101_Function extends Named {






    private List<systemworkbench101_Function> systemworkbench101_functions;




    private systemworkbench101_Function systemworkbench101_function;


    public systemworkbench101_Function(
    ) {
        super(
        );
        this.systemworkbench101_functions = new ArrayList<>();
    }

    public systemworkbench101_Function(
        ArrayList<systemworkbench101_Function> systemworkbench101_functions    ) {
        this.systemworkbench101_functions = systemworkbench101_functions;
    }


    public List<systemworkbench101_Function> getSystemworkbench101_functions() {
        return systemworkbench101_functions;
    }

    public void addSystemworkbench101_function(Systemworkbench101_function systemworkbench101_function) {
        this.systemworkbench101_functions.add(systemworkbench101_function);
    }
    public systemworkbench101_Function getSystemworkbench101_function() {
        return systemworkbench101_function;
    }

    public void setSystemworkbench101_function(systemworkbench101_Function systemworkbench101_function) {
        this.systemworkbench101_function = systemworkbench101_function;
    }

}