





import java.util.List;
import java.util.ArrayList;

public class eol_NativeExpression extends LiteralExpression {






    private eol_BooleanExpression eol_booleanexpression;




    private eol_StringExpression eol_stringexpression;


    public eol_NativeExpression(
    ) {
        super(
        );
    }



    public eol_BooleanExpression getEol_booleanexpression() {
        return eol_booleanexpression;
    }

    public void setEol_booleanexpression(eol_BooleanExpression eol_booleanexpression) {
        this.eol_booleanexpression = eol_booleanexpression;
    }
    public eol_StringExpression getEol_stringexpression() {
        return eol_stringexpression;
    }

    public void setEol_stringexpression(eol_StringExpression eol_stringexpression) {
        this.eol_stringexpression = eol_stringexpression;
    }

}