





import java.util.List;
import java.util.ArrayList;

public class EmigOcl_OclFeatureDefinition extends LocatedElement {

    private String static;





    private EmigOcl_Module emigocl_module;


    public EmigOcl_OclFeatureDefinition(
        String static    ) {
        super(
        );
        this.static = static;
    }


    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }

    public EmigOcl_Module getEmigocl_module() {
        return emigocl_module;
    }

    public void setEmigocl_module(EmigOcl_Module emigocl_module) {
        this.emigocl_module = emigocl_module;
    }

}