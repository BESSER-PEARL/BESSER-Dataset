





import java.util.List;
import java.util.ArrayList;

public class dbl_SuperClassSpecification  {






    private dbl_Clazz dbl_clazz;




    private dbl_ClassSimilar dbl_classsimilar;




    private List<dbl_Expression> dbl_expressions;


    public dbl_SuperClassSpecification(
    ) {
        this.dbl_expressions = new ArrayList<>();
    }

    public dbl_SuperClassSpecification(
        ArrayList<dbl_Expression> dbl_expressions    ) {
        this.dbl_expressions = dbl_expressions;
    }


    public dbl_Clazz getDbl_clazz() {
        return dbl_clazz;
    }

    public void setDbl_clazz(dbl_Clazz dbl_clazz) {
        this.dbl_clazz = dbl_clazz;
    }
    public dbl_ClassSimilar getDbl_classsimilar() {
        return dbl_classsimilar;
    }

    public void setDbl_classsimilar(dbl_ClassSimilar dbl_classsimilar) {
        this.dbl_classsimilar = dbl_classsimilar;
    }
    public List<dbl_Expression> getDbl_expressions() {
        return dbl_expressions;
    }

    public void addDbl_expression(Dbl_expression dbl_expression) {
        this.dbl_expressions.add(dbl_expression);
    }

}