





import java.util.List;
import java.util.ArrayList;

public class sedml_variable  {

    private String target;
    private String id;
    private String symbol;





    private sedml_listOfVariables sedml_listofvariables;




    private sedml_task sedml_task;


    public sedml_variable(
        String target,        String id,        String symbol    ) {
        this.target = target;
        this.id = id;
        this.symbol = symbol;
    }


    public String getTarget() {
        return target;
    }

    public void setTarget(String target) {
        this.target = target;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSymbol() {
        return symbol;
    }

    public void setSymbol(String symbol) {
        this.symbol = symbol;
    }

    public sedml_listOfVariables getSedml_listofvariables() {
        return sedml_listofvariables;
    }

    public void setSedml_listofvariables(sedml_listOfVariables sedml_listofvariables) {
        this.sedml_listofvariables = sedml_listofvariables;
    }
    public sedml_task getSedml_task() {
        return sedml_task;
    }

    public void setSedml_task(sedml_task sedml_task) {
        this.sedml_task = sedml_task;
    }

}