





import java.util.List;
import java.util.ArrayList;

public class systemworkbench102_FunctionProperty extends Named {

    private String description;





    private systemworkbench102_FunctionProperty systemworkbench102_functionproperty;




    private systemworkbench102_Workbench systemworkbench102_workbench;


    public systemworkbench102_FunctionProperty(
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

    public systemworkbench102_FunctionProperty getSystemworkbench102_functionproperty() {
        return systemworkbench102_functionproperty;
    }

    public void setSystemworkbench102_functionproperty(systemworkbench102_FunctionProperty systemworkbench102_functionproperty) {
        this.systemworkbench102_functionproperty = systemworkbench102_functionproperty;
    }
    public systemworkbench102_Workbench getSystemworkbench102_workbench() {
        return systemworkbench102_workbench;
    }

    public void setSystemworkbench102_workbench(systemworkbench102_Workbench systemworkbench102_workbench) {
        this.systemworkbench102_workbench = systemworkbench102_workbench;
    }

}