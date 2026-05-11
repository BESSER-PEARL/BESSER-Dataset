





import java.util.List;
import java.util.ArrayList;

public class pascal_factor  {

    private String boolean;
    private String string;
    private boolean nil;





    private pascal_term pascal_term;




    private pascal_set pascal_set;




    private pascal_variable pascal_variable;




    private pascal_number pascal_number;




    private pascal_factor pascal_factor;




    private pascal_function_designator pascal_function_designator;




    private pascal_expression pascal_expression;


    public pascal_factor(
        String boolean,        String string,        boolean nil    ) {
        this.boolean = boolean;
        this.string = string;
        this.nil = nil;
    }


    public String getBoolean() {
        return boolean;
    }

    public void setBoolean(String boolean) {
        this.boolean = boolean;
    }
    public String getString() {
        return string;
    }

    public void setString(String string) {
        this.string = string;
    }
    public boolean getNil() {
        return nil;
    }

    public void setNil(boolean nil) {
        this.nil = nil;
    }

    public pascal_term getPascal_term() {
        return pascal_term;
    }

    public void setPascal_term(pascal_term pascal_term) {
        this.pascal_term = pascal_term;
    }
    public pascal_set getPascal_set() {
        return pascal_set;
    }

    public void setPascal_set(pascal_set pascal_set) {
        this.pascal_set = pascal_set;
    }
    public pascal_variable getPascal_variable() {
        return pascal_variable;
    }

    public void setPascal_variable(pascal_variable pascal_variable) {
        this.pascal_variable = pascal_variable;
    }
    public pascal_number getPascal_number() {
        return pascal_number;
    }

    public void setPascal_number(pascal_number pascal_number) {
        this.pascal_number = pascal_number;
    }
    public pascal_factor getPascal_factor() {
        return pascal_factor;
    }

    public void setPascal_factor(pascal_factor pascal_factor) {
        this.pascal_factor = pascal_factor;
    }
    public pascal_function_designator getPascal_function_designator() {
        return pascal_function_designator;
    }

    public void setPascal_function_designator(pascal_function_designator pascal_function_designator) {
        this.pascal_function_designator = pascal_function_designator;
    }
    public pascal_expression getPascal_expression() {
        return pascal_expression;
    }

    public void setPascal_expression(pascal_expression pascal_expression) {
        this.pascal_expression = pascal_expression;
    }

}