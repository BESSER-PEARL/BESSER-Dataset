





import java.util.List;
import java.util.ArrayList;

public class expression_CollectionExpression extends Expression, FeatureCall {

    private String var;



    public expression_CollectionExpression(
        String var    ) {
        super(
        );
        this.var = var;
    }


    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }


}