





import java.util.List;
import java.util.ArrayList;

public class plSql_ProcedureDeclaration extends Item {

    private String name;





    private plSql_ParameterSequence plsql_parametersequence;


    public plSql_ProcedureDeclaration(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public plSql_ParameterSequence getPlsql_parametersequence() {
        return plsql_parametersequence;
    }

    public void setPlsql_parametersequence(plSql_ParameterSequence plsql_parametersequence) {
        this.plsql_parametersequence = plsql_parametersequence;
    }

}