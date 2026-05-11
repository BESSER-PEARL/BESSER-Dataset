





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_PathDereference extends PathExpression {






    private OPLmetamodel_Reference oplmetamodel_reference;




    private OPLmetamodel_PathExpression oplmetamodel_pathexpression;


    public OPLmetamodel_PathDereference(
    ) {
        super(
        );
    }



    public OPLmetamodel_Reference getOplmetamodel_reference() {
        return oplmetamodel_reference;
    }

    public void setOplmetamodel_reference(OPLmetamodel_Reference oplmetamodel_reference) {
        this.oplmetamodel_reference = oplmetamodel_reference;
    }
    public OPLmetamodel_PathExpression getOplmetamodel_pathexpression() {
        return oplmetamodel_pathexpression;
    }

    public void setOplmetamodel_pathexpression(OPLmetamodel_PathExpression oplmetamodel_pathexpression) {
        this.oplmetamodel_pathexpression = oplmetamodel_pathexpression;
    }

}