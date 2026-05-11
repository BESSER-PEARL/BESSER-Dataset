





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Extension extends CollectionExpression {






    private List<OPLmetamodel_Expression> oplmetamodel_expressions;


    public OPLmetamodel_Extension(
    ) {
        super(
        );
        this.oplmetamodel_expressions = new ArrayList<>();
    }

    public OPLmetamodel_Extension(
        ArrayList<OPLmetamodel_Expression> oplmetamodel_expressions    ) {
        this.oplmetamodel_expressions = oplmetamodel_expressions;
    }


    public List<OPLmetamodel_Expression> getOplmetamodel_expressions() {
        return oplmetamodel_expressions;
    }

    public void addOplmetamodel_expression(Oplmetamodel_expression oplmetamodel_expression) {
        this.oplmetamodel_expressions.add(oplmetamodel_expression);
    }

}