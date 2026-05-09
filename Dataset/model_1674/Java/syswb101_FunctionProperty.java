





import java.util.List;
import java.util.ArrayList;

public class syswb101_FunctionProperty extends Named {

    private String description;





    private syswb101_FunctionProperty syswb101_functionproperty;




    private syswb101_Workbench syswb101_workbench;




    private syswb101_Function syswb101_function;


    public syswb101_FunctionProperty(
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

    public syswb101_FunctionProperty getSyswb101_functionproperty() {
        return syswb101_functionproperty;
    }

    public void setSyswb101_functionproperty(syswb101_FunctionProperty syswb101_functionproperty) {
        this.syswb101_functionproperty = syswb101_functionproperty;
    }
    public syswb101_Workbench getSyswb101_workbench() {
        return syswb101_workbench;
    }

    public void setSyswb101_workbench(syswb101_Workbench syswb101_workbench) {
        this.syswb101_workbench = syswb101_workbench;
    }
    public syswb101_Function getSyswb101_function() {
        return syswb101_function;
    }

    public void setSyswb101_function(syswb101_Function syswb101_function) {
        this.syswb101_function = syswb101_function;
    }

}