





import java.util.List;
import java.util.ArrayList;

public class pascal_abstraction_heading extends abstraction_declaration {

    private String name;
    private String returnType;





    private pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part;


    public pascal_abstraction_heading(
        String name,        String returnType    ) {
        super(
        );
        this.name = name;
        this.returnType = returnType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }

    public pascal_procedure_and_function_declaration_part getPascal_procedure_and_function_declaration_part() {
        return pascal_procedure_and_function_declaration_part;
    }

    public void setPascal_procedure_and_function_declaration_part(pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part) {
        this.pascal_procedure_and_function_declaration_part = pascal_procedure_and_function_declaration_part;
    }

}