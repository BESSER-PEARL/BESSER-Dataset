





import java.util.List;
import java.util.ArrayList;

public class model_expression_Var extends IExpressionTerm {

    private String identifier;



    public model_expression_Var(
        String identifier    ) {
        super(
        );
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }


}