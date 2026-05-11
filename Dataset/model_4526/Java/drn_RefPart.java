





import java.util.List;
import java.util.ArrayList;

public class drn_RefPart extends Expression {

    private String params;





    private drn_Model drn_model;




    private drn_Assignement drn_assignement;


    public drn_RefPart(
        String params    ) {
        super(
        );
        this.params = params;
    }


    public String getParams() {
        return params;
    }

    public void setParams(String params) {
        this.params = params;
    }

    public drn_Model getDrn_model() {
        return drn_model;
    }

    public void setDrn_model(drn_Model drn_model) {
        this.drn_model = drn_model;
    }
    public drn_Assignement getDrn_assignement() {
        return drn_assignement;
    }

    public void setDrn_assignement(drn_Assignement drn_assignement) {
        this.drn_assignement = drn_assignement;
    }

}