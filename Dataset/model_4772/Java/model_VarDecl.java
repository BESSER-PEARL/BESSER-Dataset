





import java.util.List;
import java.util.ArrayList;

public class model_VarDecl  {

    private String var;





    private model_MOperation model_moperation;




    private model_Type model_type;


    public model_VarDecl(
        String var    ) {
        this.var = var;
    }


    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }

    public model_MOperation getModel_moperation() {
        return model_moperation;
    }

    public void setModel_moperation(model_MOperation model_moperation) {
        this.model_moperation = model_moperation;
    }
    public model_Type getModel_type() {
        return model_type;
    }

    public void setModel_type(model_Type model_type) {
        this.model_type = model_type;
    }

}