





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_ArrayDereference extends PathExpression {






    private List<OPLmetamodel_Expression> oplmetamodel_expressions;




    private OPLmetamodel_ArraySlotConstraint oplmetamodel_arrayslotconstraint;




    private OPLmetamodel_PathExpression oplmetamodel_pathexpression;


    public OPLmetamodel_ArrayDereference(
    ) {
        super(
        );
        this.oplmetamodel_expressions = new ArrayList<>();
    }

    public OPLmetamodel_ArrayDereference(
        ArrayList<OPLmetamodel_Expression> oplmetamodel_expressions    ) {
        this.oplmetamodel_expressions = oplmetamodel_expressions;
    }


    public List<OPLmetamodel_Expression> getOplmetamodel_expressions() {
        return oplmetamodel_expressions;
    }

    public void addOplmetamodel_expression(Oplmetamodel_expression oplmetamodel_expression) {
        this.oplmetamodel_expressions.add(oplmetamodel_expression);
    }
    public OPLmetamodel_ArraySlotConstraint getOplmetamodel_arrayslotconstraint() {
        return oplmetamodel_arrayslotconstraint;
    }

    public void setOplmetamodel_arrayslotconstraint(OPLmetamodel_ArraySlotConstraint oplmetamodel_arrayslotconstraint) {
        this.oplmetamodel_arrayslotconstraint = oplmetamodel_arrayslotconstraint;
    }
    public OPLmetamodel_PathExpression getOplmetamodel_pathexpression() {
        return oplmetamodel_pathexpression;
    }

    public void setOplmetamodel_pathexpression(OPLmetamodel_PathExpression oplmetamodel_pathexpression) {
        this.oplmetamodel_pathexpression = oplmetamodel_pathexpression;
    }

}