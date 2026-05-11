





import java.util.List;
import java.util.ArrayList;

public class smc_List extends Expression {






    private List<smc_Expression> smc_expressions;




    private smc_Dict smc_dict;


    public smc_List(
    ) {
        super(
        );
        this.smc_expressions = new ArrayList<>();
    }

    public smc_List(
        ArrayList<smc_Expression> smc_expressions    ) {
        this.smc_expressions = smc_expressions;
    }


    public List<smc_Expression> getSmc_expressions() {
        return smc_expressions;
    }

    public void addSmc_expression(Smc_expression smc_expression) {
        this.smc_expressions.add(smc_expression);
    }
    public smc_Dict getSmc_dict() {
        return smc_dict;
    }

    public void setSmc_dict(smc_Dict smc_dict) {
        this.smc_dict = smc_dict;
    }

}