





import java.util.List;
import java.util.ArrayList;

public class dbl_SuperClassSpecification  {






    private dbl_Class dbl_class;




    private dbl_Class dbl_class;




    private List<dbl_Expression> dbl_expressions;


    public dbl_SuperClassSpecification(
    ) {
        this.dbl_expressions = new ArrayList<>();
    }

    public dbl_SuperClassSpecification(
        ArrayList<dbl_Expression> dbl_expressions    ) {
        this.dbl_expressions = dbl_expressions;
    }


    public dbl_Class getDbl_class() {
        return dbl_class;
    }

    public void setDbl_class(dbl_Class dbl_class) {
        this.dbl_class = dbl_class;
    }
    public dbl_Class getDbl_class() {
        return dbl_class;
    }

    public void setDbl_class(dbl_Class dbl_class) {
        this.dbl_class = dbl_class;
    }
    public List<dbl_Expression> getDbl_expressions() {
        return dbl_expressions;
    }

    public void addDbl_expression(Dbl_expression dbl_expression) {
        this.dbl_expressions.add(dbl_expression);
    }

}