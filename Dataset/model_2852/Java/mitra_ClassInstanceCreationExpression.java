





import java.util.List;
import java.util.ArrayList;

public class mitra_ClassInstanceCreationExpression extends TerminalExpression, StatementExpression {






    private mitra_Type mitra_type;




    private List<mitra_Expression> mitra_expressions;


    public mitra_ClassInstanceCreationExpression(
    ) {
        super(
        );
        this.mitra_expressions = new ArrayList<>();
    }

    public mitra_ClassInstanceCreationExpression(
        ArrayList<mitra_Expression> mitra_expressions    ) {
        this.mitra_expressions = mitra_expressions;
    }


    public mitra_Type getMitra_type() {
        return mitra_type;
    }

    public void setMitra_type(mitra_Type mitra_type) {
        this.mitra_type = mitra_type;
    }
    public List<mitra_Expression> getMitra_expressions() {
        return mitra_expressions;
    }

    public void addMitra_expression(Mitra_expression mitra_expression) {
        this.mitra_expressions.add(mitra_expression);
    }

}