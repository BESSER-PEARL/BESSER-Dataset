





import java.util.List;
import java.util.ArrayList;

public class simpleocl_OclMetamodel extends OclModel {

    private String uri;





    private simpleocl_OclInstanceModel simpleocl_oclinstancemodel;




    private List<simpleocl_OclInstanceModel> simpleocl_oclinstancemodels;


    public simpleocl_OclMetamodel(
        String uri    ) {
        super(
        );
        this.uri = uri;
        this.simpleocl_oclinstancemodels = new ArrayList<>();
    }

    public simpleocl_OclMetamodel(
        String uri        ArrayList<simpleocl_OclInstanceModel> simpleocl_oclinstancemodels    ) {
        this.uri = uri;
        this.simpleocl_oclinstancemodels = simpleocl_oclinstancemodels;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public simpleocl_OclInstanceModel getSimpleocl_oclinstancemodel() {
        return simpleocl_oclinstancemodel;
    }

    public void setSimpleocl_oclinstancemodel(simpleocl_OclInstanceModel simpleocl_oclinstancemodel) {
        this.simpleocl_oclinstancemodel = simpleocl_oclinstancemodel;
    }
    public List<simpleocl_OclInstanceModel> getSimpleocl_oclinstancemodels() {
        return simpleocl_oclinstancemodels;
    }

    public void addSimpleocl_oclinstancemodel(Simpleocl_oclinstancemodel simpleocl_oclinstancemodel) {
        this.simpleocl_oclinstancemodels.add(simpleocl_oclinstancemodel);
    }

}