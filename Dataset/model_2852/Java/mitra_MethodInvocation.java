





import java.util.List;
import java.util.ArrayList;

public class mitra_MethodInvocation extends Feature {






    private List<mitra_Expression> mitra_expressions;


    public mitra_MethodInvocation(
    ) {
        super(
        );
        this.mitra_expressions = new ArrayList<>();
    }

    public mitra_MethodInvocation(
        ArrayList<mitra_Expression> mitra_expressions    ) {
        this.mitra_expressions = mitra_expressions;
    }


    public List<mitra_Expression> getMitra_expressions() {
        return mitra_expressions;
    }

    public void addMitra_expression(Mitra_expression mitra_expression) {
        this.mitra_expressions.add(mitra_expression);
    }

}