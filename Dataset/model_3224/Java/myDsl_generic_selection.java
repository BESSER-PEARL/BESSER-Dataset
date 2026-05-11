





import java.util.List;
import java.util.ArrayList;

public class myDsl_generic_selection  {

    private String _generic;





    private myDsl_primary_expression mydsl_primary_expression;


    public myDsl_generic_selection(
        String _generic    ) {
        this._generic = _generic;
    }


    public String get_generic() {
        return _generic;
    }

    public void set_generic(String _generic) {
        this._generic = _generic;
    }

    public myDsl_primary_expression getMydsl_primary_expression() {
        return mydsl_primary_expression;
    }

    public void setMydsl_primary_expression(myDsl_primary_expression mydsl_primary_expression) {
        this.mydsl_primary_expression = mydsl_primary_expression;
    }

}