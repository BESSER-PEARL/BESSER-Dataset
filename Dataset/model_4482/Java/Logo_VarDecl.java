





import java.util.List;
import java.util.ArrayList;

public class Logo_VarDecl extends Instruction {

    private String name;





    private Logo_Assignation logo_assignation;




    private Logo_Expression logo_expression;


    public Logo_VarDecl(
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

    public Logo_Assignation getLogo_assignation() {
        return logo_assignation;
    }

    public void setLogo_assignation(Logo_Assignation logo_assignation) {
        this.logo_assignation = logo_assignation;
    }
    public Logo_Expression getLogo_expression() {
        return logo_expression;
    }

    public void setLogo_expression(Logo_Expression logo_expression) {
        this.logo_expression = logo_expression;
    }

}