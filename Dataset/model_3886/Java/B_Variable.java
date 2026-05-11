





import java.util.List;
import java.util.ArrayList;

public class B_Variable  {

    private String name;





    private B_Machine b_machine;




    private B_Variable b_variable;




    private B_VariableList b_variablelist;




    private B_VariableList b_variablelist;




    private B_Any b_any;




    private B_Predicate b_predicate;


    public B_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public B_Machine getB_machine() {
        return b_machine;
    }

    public void setB_machine(B_Machine b_machine) {
        this.b_machine = b_machine;
    }
    public B_Variable getB_variable() {
        return b_variable;
    }

    public void setB_variable(B_Variable b_variable) {
        this.b_variable = b_variable;
    }
    public B_VariableList getB_variablelist() {
        return b_variablelist;
    }

    public void setB_variablelist(B_VariableList b_variablelist) {
        this.b_variablelist = b_variablelist;
    }
    public B_VariableList getB_variablelist() {
        return b_variablelist;
    }

    public void setB_variablelist(B_VariableList b_variablelist) {
        this.b_variablelist = b_variablelist;
    }
    public B_Any getB_any() {
        return b_any;
    }

    public void setB_any(B_Any b_any) {
        this.b_any = b_any;
    }
    public B_Predicate getB_predicate() {
        return b_predicate;
    }

    public void setB_predicate(B_Predicate b_predicate) {
        this.b_predicate = b_predicate;
    }

}