





import java.util.List;
import java.util.ArrayList;

public class pascal_factor  {

    private boolean nil;
    private String string;
    private String boolean;





    private pascal_function_designator pascal_function_designator;




    private pascal_term pascal_term;




    private pascal_expression pascal_expression;




    private pascal_variable pascal_variable;




    private pascal_factor pascal_factor;


    public pascal_factor(
        boolean nil,        String string,        String boolean    ) {
        this.nil = nil;
        this.string = string;
        this.boolean = boolean;
    }


    public boolean getNil() {
        return nil;
    }

    public void setNil(boolean nil) {
        this.nil = nil;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public String getBoolean() {
        return boolean;
    }

    public void setBoolean(String boolean) {
        this.boolean = boolean;
    }

    public pascal_function_designator getPascal_function_designator() {
        return pascal_function_designator;
    }

    public void setPascal_function_designator(pascal_function_designator pascal_function_designator) {
        this.pascal_function_designator = pascal_function_designator;
    }
    public pascal_term getPascal_term() {
        return pascal_term;
    }

    public void setPascal_term(pascal_term pascal_term) {
        this.pascal_term = pascal_term;
    }
    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }
    public pascal_variable getPascal_variable() {
        return pascal_variable;
    }

    public void setPascal_variable(pascal_variable pascal_variable) {
        this.pascal_variable = pascal_variable;
    }
    public pascal_factor getPascal_factor() {
        return pascal_factor;
    }

    public void setPascal_factor(pascal_factor pascal_factor) {
        this.pascal_factor = pascal_factor;
    }

}