





import java.util.List;
import java.util.ArrayList;

public class OPLmetamodel_Objective extends Declaration {

    private boolean isLinearRelaxation;
    private String action;



    public OPLmetamodel_Objective(
        boolean isLinearRelaxation,        String action    ) {
        super(
        );
        this.isLinearRelaxation = isLinearRelaxation;
        this.action = action;
    }


    public boolean getIslinearrelaxation() {
        return isLinearRelaxation;
    }

    public void setIslinearrelaxation(boolean isLinearRelaxation) {
        this.isLinearRelaxation = isLinearRelaxation;
    }
    public String getAction() {
        return action;
    }

    public void setAction(String action) {
        this.action = action;
    }


}