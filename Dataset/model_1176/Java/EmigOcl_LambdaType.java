





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_LambdaType extends OclType {






    private List<EmigOcl_OclType> emigocl_ocltypes;




    private EmigOcl_OclType emigocl_ocltype;


    public EmigOcl_LambdaType(
    ) {
        super(
        );
        this.emigocl_ocltypes = new ArrayList<>();
    }

    public EmigOcl_LambdaType(
        ArrayList<EmigOcl_OclType> emigocl_ocltypes    ) {
        this.emigocl_ocltypes = emigocl_ocltypes;
    }


    public List<EmigOcl_OclType> getEmigocl_ocltypes() {
        return emigocl_ocltypes;
    }

    public void addEmigocl_ocltype(Emigocl_ocltype emigocl_ocltype) {
        this.emigocl_ocltypes.add(emigocl_ocltype);
    }
    public EmigOcl_OclType getEmigocl_ocltype() {
        return emigocl_ocltype;
    }

    public void setEmigocl_ocltype(EmigOcl_OclType emigocl_ocltype) {
        this.emigocl_ocltype = emigocl_ocltype;
    }

}