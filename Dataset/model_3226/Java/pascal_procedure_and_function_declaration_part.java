





import java.util.List;
import java.util.ArrayList;

public class pascal_procedure_and_function_declaration_part  {






    private List<pascal_function_declaration> pascal_function_declarations;




    private pascal_DeclarationPart pascal_declarationpart;




    private List<pascal_procedure_declaration> pascal_procedure_declarations;


    public pascal_procedure_and_function_declaration_part(
    ) {
        this.pascal_function_declarations = new ArrayList<>();
        this.pascal_procedure_declarations = new ArrayList<>();
    }

    public pascal_procedure_and_function_declaration_part(
        ArrayList<pascal_function_declaration> pascal_function_declarations,        ArrayList<pascal_procedure_declaration> pascal_procedure_declarations    ) {
        this.pascal_function_declarations = pascal_function_declarations;
        this.pascal_procedure_declarations = pascal_procedure_declarations;
    }


    public List<pascal_function_declaration> getPascal_function_declarations() {
        return pascal_function_declarations;
    }

    public void addPascal_function_declaration(Pascal_function_declaration pascal_function_declaration) {
        this.pascal_function_declarations.add(pascal_function_declaration);
    }
    public pascal_DeclarationPart getPascal_declarationpart() {
        return pascal_declarationpart;
    }

    public void setPascal_declarationpart(pascal_DeclarationPart pascal_declarationpart) {
        this.pascal_declarationpart = pascal_declarationpart;
    }
    public List<pascal_procedure_declaration> getPascal_procedure_declarations() {
        return pascal_procedure_declarations;
    }

    public void addPascal_procedure_declaration(Pascal_procedure_declaration pascal_procedure_declaration) {
        this.pascal_procedure_declarations.add(pascal_procedure_declaration);
    }

}