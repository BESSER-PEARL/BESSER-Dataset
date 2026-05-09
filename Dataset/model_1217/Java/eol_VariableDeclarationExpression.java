





import java.util.List;
import java.util.ArrayList;

public class eol_VariableDeclarationExpression extends Expression {

    private boolean create;





    private eol_NameExpression eol_nameexpression;




    private List<eol_NameExpression> eol_nameexpressions;


    public eol_VariableDeclarationExpression(
        boolean create    ) {
        super(
        );
        this.create = create;
        this.eol_nameexpressions = new ArrayList<>();
    }

    public eol_VariableDeclarationExpression(
        boolean create        ArrayList<eol_NameExpression> eol_nameexpressions    ) {
        this.create = create;
        this.eol_nameexpressions = eol_nameexpressions;
    }

    public boolean getCreate() {
        return create;
    }

    public void setCreate(boolean create) {
        this.create = create;
    }

    public eol_NameExpression getEol_nameexpression() {
        return eol_nameexpression;
    }

    public void setEol_nameexpression(eol_NameExpression eol_nameexpression) {
        this.eol_nameexpression = eol_nameexpression;
    }
    public List<eol_NameExpression> getEol_nameexpressions() {
        return eol_nameexpressions;
    }

    public void addEol_nameexpression(Eol_nameexpression eol_nameexpression) {
        this.eol_nameexpressions.add(eol_nameexpression);
    }

}