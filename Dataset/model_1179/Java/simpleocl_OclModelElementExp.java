





import java.util.List;
import java.util.ArrayList;

public class simpleocl_OclModelElementExp extends OclExpression {

    private String name;





    private simpleocl_OclModel simpleocl_oclmodel;


    public simpleocl_OclModelElementExp(
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

    public simpleocl_OclModel getSimpleocl_oclmodel() {
        return simpleocl_oclmodel;
    }

    public void setSimpleocl_oclmodel(simpleocl_OclModel simpleocl_oclmodel) {
        this.simpleocl_oclmodel = simpleocl_oclmodel;
    }

}