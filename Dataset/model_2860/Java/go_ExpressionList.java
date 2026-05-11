





import java.util.List;
import java.util.ArrayList;

public class go_ExpressionList  {






    private go_ConstSpec go_constspec;




    private List<go_Expression> go_expressions;




    private go_VarSpec go_varspec;


    public go_ExpressionList(
    ) {
        this.go_expressions = new ArrayList<>();
    }

    public go_ExpressionList(
        ArrayList<go_Expression> go_expressions    ) {
        this.go_expressions = go_expressions;
    }


    public go_ConstSpec getGo_constspec() {
        return go_constspec;
    }

    public void setGo_constspec(go_ConstSpec go_constspec) {
        this.go_constspec = go_constspec;
    }
    public List<go_Expression> getGo_expressions() {
        return go_expressions;
    }

    public void addGo_expression(Go_expression go_expression) {
        this.go_expressions.add(go_expression);
    }
    public go_VarSpec getGo_varspec() {
        return go_varspec;
    }

    public void setGo_varspec(go_VarSpec go_varspec) {
        this.go_varspec = go_varspec;
    }

}