





import java.util.List;
import java.util.ArrayList;

public class plSql_ParameterSequence  {






    private plSql_Procedure plsql_procedure;




    private plSql_Function plsql_function;




    private List<plSql_ParameterDeclaration> plsql_parameterdeclarations;




    private plSql_ProcedureDefinition plsql_proceduredefinition;


    public plSql_ParameterSequence(
    ) {
        this.plsql_parameterdeclarations = new ArrayList<>();
    }

    public plSql_ParameterSequence(
        ArrayList<plSql_ParameterDeclaration> plsql_parameterdeclarations    ) {
        this.plsql_parameterdeclarations = plsql_parameterdeclarations;
    }


    public plSql_Procedure getPlsql_procedure() {
        return plsql_procedure;
    }

    public void setPlsql_procedure(plSql_Procedure plsql_procedure) {
        this.plsql_procedure = plsql_procedure;
    }
    public plSql_Function getPlsql_function() {
        return plsql_function;
    }

    public void setPlsql_function(plSql_Function plsql_function) {
        this.plsql_function = plsql_function;
    }
    public List<plSql_ParameterDeclaration> getPlsql_parameterdeclarations() {
        return plsql_parameterdeclarations;
    }

    public void addPlsql_parameterdeclaration(Plsql_parameterdeclaration plsql_parameterdeclaration) {
        this.plsql_parameterdeclarations.add(plsql_parameterdeclaration);
    }
    public plSql_ProcedureDefinition getPlsql_proceduredefinition() {
        return plsql_proceduredefinition;
    }

    public void setPlsql_proceduredefinition(plSql_ProcedureDefinition plsql_proceduredefinition) {
        this.plsql_proceduredefinition = plsql_proceduredefinition;
    }

}