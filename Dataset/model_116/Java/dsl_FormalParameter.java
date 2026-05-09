





import java.util.List;
import java.util.ArrayList;

public class dsl_FormalParameter  {

    private boolean final;





    private dsl_FormalParameters dsl_formalparameters;




    private dsl_Type dsl_type;


    public dsl_FormalParameter(
        boolean final    ) {
        this.final = final;
    }


    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }

    public dsl_FormalParameters getDsl_formalparameters() {
        return dsl_formalparameters;
    }

    public void setDsl_formalparameters(dsl_FormalParameters dsl_formalparameters) {
        this.dsl_formalparameters = dsl_formalparameters;
    }
    public dsl_Type getDsl_type() {
        return dsl_type;
    }

    public void setDsl_type(dsl_Type dsl_type) {
        this.dsl_type = dsl_type;
    }

}