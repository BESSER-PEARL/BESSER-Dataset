





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_AllExpression  {






    private List<OPLmetamodel_FormalParameter> oplmetamodel_formalparameters;




    private OPLmetamodel_Expression oplmetamodel_expression;


    public OPLmetamodel_AllExpression(
    ) {
        this.oplmetamodel_formalparameters = new ArrayList<>();
    }

    public OPLmetamodel_AllExpression(
        ArrayList<OPLmetamodel_FormalParameter> oplmetamodel_formalparameters    ) {
        this.oplmetamodel_formalparameters = oplmetamodel_formalparameters;
    }


    public List<OPLmetamodel_FormalParameter> getOplmetamodel_formalparameters() {
        return oplmetamodel_formalparameters;
    }

    public void addOplmetamodel_formalparameter(Oplmetamodel_formalparameter oplmetamodel_formalparameter) {
        this.oplmetamodel_formalparameters.add(oplmetamodel_formalparameter);
    }
    public OPLmetamodel_Expression getOplmetamodel_expression() {
        return oplmetamodel_expression;
    }

    public void setOplmetamodel_expression(OPLmetamodel_Expression oplmetamodel_expression) {
        this.oplmetamodel_expression = oplmetamodel_expression;
    }

}