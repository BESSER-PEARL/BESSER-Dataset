





import java.util.List;
import java.util.ArrayList;

public class pascal_abstraction_heading extends abstraction_declaration {

    private String resultType;
    private String name;





    private pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part;


    public pascal_abstraction_heading(
        String resultType,        String name    ) {
        super(
        );
        this.resultType = resultType;
        this.name = name;
    }


    public String getResulttype() {
        return resultType;
    }

    public void setResulttype(String resultType) {
        this.resultType = resultType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public pascal_procedure_and_function_declaration_part getPascal_procedure_and_function_declaration_part() {
        return pascal_procedure_and_function_declaration_part;
    }

    public void setPascal_procedure_and_function_declaration_part(pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part) {
        this.pascal_procedure_and_function_declaration_part = pascal_procedure_and_function_declaration_part;
    }

}