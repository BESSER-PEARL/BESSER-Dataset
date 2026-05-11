





import java.util.List;
import java.util.ArrayList;

public class plSql_ProcedureDefinition extends Item, NameDeclaration {






    private plSql_ProcedureImplementation plsql_procedureimplementation;


    public plSql_ProcedureDefinition(
    ) {
        super(
        );
    }



    public plSql_ProcedureImplementation getPlsql_procedureimplementation() {
        return plsql_procedureimplementation;
    }

    public void setPlsql_procedureimplementation(plSql_ProcedureImplementation plsql_procedureimplementation) {
        this.plsql_procedureimplementation = plsql_procedureimplementation;
    }

}