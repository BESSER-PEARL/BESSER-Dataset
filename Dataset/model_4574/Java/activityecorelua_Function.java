





import java.util.List;
import java.util.ArrayList;

public class activityecorelua_Function  {

    private String parameters;
    private boolean varArgs;





    private activityecorelua_Statement_LocalFunction_Declaration activityecorelua_statement_localfunction_declaration;




    private activityecorelua_Statement_GlobalFunction_Declaration activityecorelua_statement_globalfunction_declaration;




    private activityecorelua_Block activityecorelua_block;


    public activityecorelua_Function(
        String parameters,        boolean varArgs    ) {
        this.parameters = parameters;
        this.varArgs = varArgs;
    }


    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }
    public boolean getVarargs() {
        return varArgs;
    }

    public void setVarargs(boolean varArgs) {
        this.varArgs = varArgs;
    }

    public activityecorelua_Statement_LocalFunction_Declaration getActivityecorelua_statement_localfunction_declaration() {
        return activityecorelua_statement_localfunction_declaration;
    }

    public void setActivityecorelua_statement_localfunction_declaration(activityecorelua_Statement_LocalFunction_Declaration activityecorelua_statement_localfunction_declaration) {
        this.activityecorelua_statement_localfunction_declaration = activityecorelua_statement_localfunction_declaration;
    }
    public activityecorelua_Statement_GlobalFunction_Declaration getActivityecorelua_statement_globalfunction_declaration() {
        return activityecorelua_statement_globalfunction_declaration;
    }

    public void setActivityecorelua_statement_globalfunction_declaration(activityecorelua_Statement_GlobalFunction_Declaration activityecorelua_statement_globalfunction_declaration) {
        this.activityecorelua_statement_globalfunction_declaration = activityecorelua_statement_globalfunction_declaration;
    }
    public activityecorelua_Block getActivityecorelua_block() {
        return activityecorelua_block;
    }

    public void setActivityecorelua_block(activityecorelua_Block activityecorelua_block) {
        this.activityecorelua_block = activityecorelua_block;
    }

}