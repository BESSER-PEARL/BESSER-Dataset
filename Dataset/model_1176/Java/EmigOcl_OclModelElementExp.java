





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_OclModelElementExp extends OclExpression {

    private String name;





    private EmigOcl_OclModel emigocl_oclmodel;


    public EmigOcl_OclModelElementExp(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public EmigOcl_OclModel getEmigocl_oclmodel() {
        return emigocl_oclmodel;
    }

    public void setEmigocl_oclmodel(EmigOcl_OclModel emigocl_oclmodel) {
        this.emigocl_oclmodel = emigocl_oclmodel;
    }

}