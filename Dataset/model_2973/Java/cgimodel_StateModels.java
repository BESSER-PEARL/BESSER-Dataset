





import java.util.List;
import java.util.ArrayList;

public class cgimodel_StateModels  {






    private List<cgimodel_StateModel> cgimodel_statemodels;


    public cgimodel_StateModels(
    ) {
        this.cgimodel_statemodels = new ArrayList<>();
    }

    public cgimodel_StateModels(
        ArrayList<cgimodel_StateModel> cgimodel_statemodels    ) {
        this.cgimodel_statemodels = cgimodel_statemodels;
    }


    public List<cgimodel_StateModel> getCgimodel_statemodels() {
        return cgimodel_statemodels;
    }

    public void addCgimodel_statemodel(Cgimodel_statemodel cgimodel_statemodel) {
        this.cgimodel_statemodels.add(cgimodel_statemodel);
    }

}