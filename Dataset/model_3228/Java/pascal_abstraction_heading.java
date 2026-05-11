





import java.util.List;
import java.util.ArrayList;

public class pascal_abstraction_heading extends abstraction_declaration {

    private String name;
    private String resultType;





    private pascal_formal_parameter_list pascal_formal_parameter_list;




    private pascal_formal_parameter_section pascal_formal_parameter_section;




    private pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part;




    private pascal_formal_parameter_section pascal_formal_parameter_section;


    public pascal_abstraction_heading(
        String name,        String resultType    ) {
        super(
        );
        this.name = name;
        this.resultType = resultType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getResulttype() {
        return resultType;
    }

    public void setResulttype(String resultType) {
        this.resultType = resultType;
    }

    public pascal_formal_parameter_list getPascal_formal_parameter_list() {
        return pascal_formal_parameter_list;
    }

    public void setPascal_formal_parameter_list(pascal_formal_parameter_list pascal_formal_parameter_list) {
        this.pascal_formal_parameter_list = pascal_formal_parameter_list;
    }
    public pascal_formal_parameter_section getPascal_formal_parameter_section() {
        return pascal_formal_parameter_section;
    }

    public void setPascal_formal_parameter_section(pascal_formal_parameter_section pascal_formal_parameter_section) {
        this.pascal_formal_parameter_section = pascal_formal_parameter_section;
    }
    public pascal_procedure_and_function_declaration_part getPascal_procedure_and_function_declaration_part() {
        return pascal_procedure_and_function_declaration_part;
    }

    public void setPascal_procedure_and_function_declaration_part(pascal_procedure_and_function_declaration_part pascal_procedure_and_function_declaration_part) {
        this.pascal_procedure_and_function_declaration_part = pascal_procedure_and_function_declaration_part;
    }
    public pascal_formal_parameter_section getPascal_formal_parameter_section() {
        return pascal_formal_parameter_section;
    }

    public void setPascal_formal_parameter_section(pascal_formal_parameter_section pascal_formal_parameter_section) {
        this.pascal_formal_parameter_section = pascal_formal_parameter_section;
    }

}