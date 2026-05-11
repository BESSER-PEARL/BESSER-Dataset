





import java.util.List;
import java.util.ArrayList;

public class arithmetics_Module  {

    private String name;





    private List<arithmetics_Statement> arithmetics_statements;




    private List<arithmetics_Import> arithmetics_imports;


    public arithmetics_Module(
        String name    ) {
        this.name = name;
        this.arithmetics_statements = new ArrayList<>();
        this.arithmetics_imports = new ArrayList<>();
    }

    public arithmetics_Module(
        String name        ArrayList<arithmetics_Statement> arithmetics_statements,        ArrayList<arithmetics_Import> arithmetics_imports    ) {
        this.name = name;
        this.arithmetics_statements = arithmetics_statements;
        this.arithmetics_imports = arithmetics_imports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<arithmetics_Statement> getArithmetics_statements() {
        return arithmetics_statements;
    }

    public void addArithmetics_statement(Arithmetics_statement arithmetics_statement) {
        this.arithmetics_statements.add(arithmetics_statement);
    }
    public List<arithmetics_Import> getArithmetics_imports() {
        return arithmetics_imports;
    }

    public void addArithmetics_import(Arithmetics_import arithmetics_import) {
        this.arithmetics_imports.add(arithmetics_import);
    }

}