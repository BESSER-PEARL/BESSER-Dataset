





import java.util.List;
import java.util.ArrayList;

public class arithmetic_Module  {

    private String name;





    private List<arithmetic_Statement> arithmetic_statements;




    private List<arithmetic_Import> arithmetic_imports;




    private arithmetic_Import arithmetic_import;


    public arithmetic_Module(
        String name    ) {
        this.name = name;
        this.arithmetic_statements = new ArrayList<>();
        this.arithmetic_imports = new ArrayList<>();
    }

    public arithmetic_Module(
        String name        ArrayList<arithmetic_Statement> arithmetic_statements,        ArrayList<arithmetic_Import> arithmetic_imports    ) {
        this.name = name;
        this.arithmetic_statements = arithmetic_statements;
        this.arithmetic_imports = arithmetic_imports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<arithmetic_Statement> getArithmetic_statements() {
        return arithmetic_statements;
    }

    public void addArithmetic_statement(Arithmetic_statement arithmetic_statement) {
        this.arithmetic_statements.add(arithmetic_statement);
    }
    public List<arithmetic_Import> getArithmetic_imports() {
        return arithmetic_imports;
    }

    public void addArithmetic_import(Arithmetic_import arithmetic_import) {
        this.arithmetic_imports.add(arithmetic_import);
    }
    public arithmetic_Import getArithmetic_import() {
        return arithmetic_import;
    }

    public void setArithmetic_import(arithmetic_Import arithmetic_import) {
        this.arithmetic_import = arithmetic_import;
    }

}