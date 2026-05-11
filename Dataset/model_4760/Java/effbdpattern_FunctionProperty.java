





import java.util.List;
import java.util.ArrayList;

public class effbdpattern_FunctionProperty  {

    private String description;





    private effbdpattern_Function effbdpattern_function;




    private effbdpattern_FunctionProperty effbdpattern_functionproperty;


    public effbdpattern_FunctionProperty(
        String description    ) {
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public effbdpattern_Function getEffbdpattern_function() {
        return effbdpattern_function;
    }

    public void setEffbdpattern_function(effbdpattern_Function effbdpattern_function) {
        this.effbdpattern_function = effbdpattern_function;
    }
    public effbdpattern_FunctionProperty getEffbdpattern_functionproperty() {
        return effbdpattern_functionproperty;
    }

    public void setEffbdpattern_functionproperty(effbdpattern_FunctionProperty effbdpattern_functionproperty) {
        this.effbdpattern_functionproperty = effbdpattern_functionproperty;
    }

}