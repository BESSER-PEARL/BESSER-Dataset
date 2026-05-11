





import java.util.List;
import java.util.ArrayList;

public class iot2_Function  {

    private boolean varArgs;
    private String parameters;





    private iot2_Statement_GlobalFunction_Declaration iot2_statement_globalfunction_declaration;




    private iot2_Block iot2_block;




    private iot2_Statement_LocalFunction_Declaration iot2_statement_localfunction_declaration;


    public iot2_Function(
        boolean varArgs,        String parameters    ) {
        this.varArgs = varArgs;
        this.parameters = parameters;
    }


    public boolean getVarargs() {
        return varArgs;
    }

    public void setVarargs(boolean varArgs) {
        this.varArgs = varArgs;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public iot2_Statement_GlobalFunction_Declaration getIot2_statement_globalfunction_declaration() {
        return iot2_statement_globalfunction_declaration;
    }

    public void setIot2_statement_globalfunction_declaration(iot2_Statement_GlobalFunction_Declaration iot2_statement_globalfunction_declaration) {
        this.iot2_statement_globalfunction_declaration = iot2_statement_globalfunction_declaration;
    }
    public iot2_Block getIot2_block() {
        return iot2_block;
    }

    public void setIot2_block(iot2_Block iot2_block) {
        this.iot2_block = iot2_block;
    }
    public iot2_Statement_LocalFunction_Declaration getIot2_statement_localfunction_declaration() {
        return iot2_statement_localfunction_declaration;
    }

    public void setIot2_statement_localfunction_declaration(iot2_Statement_LocalFunction_Declaration iot2_statement_localfunction_declaration) {
        this.iot2_statement_localfunction_declaration = iot2_statement_localfunction_declaration;
    }

}