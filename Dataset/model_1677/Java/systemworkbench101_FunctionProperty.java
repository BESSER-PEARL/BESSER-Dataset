





import java.util.List;
import java.util.ArrayList;

public class systemworkbench101_FunctionProperty extends Named {

    private String description;





    private systemworkbench101_FunctionProperty systemworkbench101_functionproperty;




    private systemworkbench101_Workbench systemworkbench101_workbench;




    private systemworkbench101_Function systemworkbench101_function;


    public systemworkbench101_FunctionProperty(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public systemworkbench101_FunctionProperty getSystemworkbench101_functionproperty() {
        return systemworkbench101_functionproperty;
    }

    public void setSystemworkbench101_functionproperty(systemworkbench101_FunctionProperty systemworkbench101_functionproperty) {
        this.systemworkbench101_functionproperty = systemworkbench101_functionproperty;
    }
    public systemworkbench101_Workbench getSystemworkbench101_workbench() {
        return systemworkbench101_workbench;
    }

    public void setSystemworkbench101_workbench(systemworkbench101_Workbench systemworkbench101_workbench) {
        this.systemworkbench101_workbench = systemworkbench101_workbench;
    }
    public systemworkbench101_Function getSystemworkbench101_function() {
        return systemworkbench101_function;
    }

    public void setSystemworkbench101_function(systemworkbench101_Function systemworkbench101_function) {
        this.systemworkbench101_function = systemworkbench101_function;
    }

}