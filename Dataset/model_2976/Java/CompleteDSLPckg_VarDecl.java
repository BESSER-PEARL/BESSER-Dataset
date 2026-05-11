





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_VarDecl extends Statement {

    private String name;





    private CompleteDSLPckg_Assignation completedslpckg_assignation;




    private CompleteDSLPckg_Expression completedslpckg_expression;


    public CompleteDSLPckg_VarDecl(
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

    public CompleteDSLPckg_Assignation getCompletedslpckg_assignation() {
        return completedslpckg_assignation;
    }

    public void setCompletedslpckg_assignation(CompleteDSLPckg_Assignation completedslpckg_assignation) {
        this.completedslpckg_assignation = completedslpckg_assignation;
    }
    public CompleteDSLPckg_Expression getCompletedslpckg_expression() {
        return completedslpckg_expression;
    }

    public void setCompletedslpckg_expression(CompleteDSLPckg_Expression completedslpckg_expression) {
        this.completedslpckg_expression = completedslpckg_expression;
    }

}