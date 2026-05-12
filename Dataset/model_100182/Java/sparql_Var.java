





import java.util.List;
import java.util.ArrayList;

public class sparql_Var extends OrderConditionRightNE, VarOrTerm, PrimaryExpression, VarOrIRIref {

    private String varname;



    public sparql_Var(
        String varname    ) {
        super(
        );
        this.varname = varname;
    }


    public String getVarname() {
        return varname;
    }

    public void setVarname(String varname) {
        this.varname = varname;
    }


}