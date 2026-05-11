





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_ForAllConstraint extends Constraint {






    private List<OPLmetamodel_Constraint> oplmetamodel_constraints;




    private List<OPLmetamodel_FormalParameter> oplmetamodel_formalparameters;


    public OPLmetamodel_ForAllConstraint(
    ) {
        super(
        );
        this.oplmetamodel_constraints = new ArrayList<>();
        this.oplmetamodel_formalparameters = new ArrayList<>();
    }

    public OPLmetamodel_ForAllConstraint(
        ArrayList<OPLmetamodel_Constraint> oplmetamodel_constraints,        ArrayList<OPLmetamodel_FormalParameter> oplmetamodel_formalparameters    ) {
        this.oplmetamodel_constraints = oplmetamodel_constraints;
        this.oplmetamodel_formalparameters = oplmetamodel_formalparameters;
    }


    public List<OPLmetamodel_Constraint> getOplmetamodel_constraints() {
        return oplmetamodel_constraints;
    }

    public void addOplmetamodel_constraint(Oplmetamodel_constraint oplmetamodel_constraint) {
        this.oplmetamodel_constraints.add(oplmetamodel_constraint);
    }
    public List<OPLmetamodel_FormalParameter> getOplmetamodel_formalparameters() {
        return oplmetamodel_formalparameters;
    }

    public void addOplmetamodel_formalparameter(Oplmetamodel_formalparameter oplmetamodel_formalparameter) {
        this.oplmetamodel_formalparameters.add(oplmetamodel_formalparameter);
    }

}