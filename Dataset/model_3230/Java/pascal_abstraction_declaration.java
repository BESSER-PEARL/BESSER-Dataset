





import java.util.List;
import java.util.ArrayList;

public class pascal_abstraction_declaration  {

    private boolean forward;





    private pascal_abstraction_heading pascal_abstraction_heading;




    private pascal_block pascal_block;




    private pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part;


    public pascal_abstraction_declaration(
        boolean forward    ) {
        this.forward = forward;
    }


    public boolean getForward() {
        return forward;
    }

    public void setForward(boolean forward) {
        this.forward = forward;
    }

    public pascal_abstraction_heading getPascal_abstraction_heading() {
        return pascal_abstraction_heading;
    }

    public void setPascal_abstraction_heading(pascal_abstraction_heading pascal_abstraction_heading) {
        this.pascal_abstraction_heading = pascal_abstraction_heading;
    }
    public pascal_block getPascal_block() {
        return pascal_block;
    }

    public void setPascal_block(pascal_block pascal_block) {
        this.pascal_block = pascal_block;
    }
    public pascal_procedure_and_function_declaration_part getPascal_procedure_and_function_declaration_part() {
        return pascal_procedure_and_function_declaration_part;
    }

    public void setPascal_procedure_and_function_declaration_part(pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part) {
        this.pascal_procedure_and_function_declaration_part = pascal_procedure_and_function_declaration_part;
    }

}