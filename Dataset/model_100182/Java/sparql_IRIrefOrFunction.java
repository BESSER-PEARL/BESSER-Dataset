





import java.util.List;
import java.util.ArrayList;

public class sparql_IRIrefOrFunction extends PrimaryExpression {






    private sparql_ArgList sparql_arglist;




    private sparql_IRIreference sparql_irireference;


    public sparql_IRIrefOrFunction(
    ) {
        super(
        );
    }



    public sparql_ArgList getSparql_arglist() {
        return sparql_arglist;
    }

    public void setSparql_arglist(sparql_ArgList sparql_arglist) {
        this.sparql_arglist = sparql_arglist;
    }
    public sparql_IRIreference getSparql_irireference() {
        return sparql_irireference;
    }

    public void setSparql_irireference(sparql_IRIreference sparql_irireference) {
        this.sparql_irireference = sparql_irireference;
    }

}