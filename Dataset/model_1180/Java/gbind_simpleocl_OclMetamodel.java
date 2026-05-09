





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_OclMetamodel extends OclModel {

    private String uri;





    private List<OclInstanceModel> oclinstancemodels;


    public gbind_simpleocl_OclMetamodel(
        String uri    ) {
        super(
        );
        this.uri = uri;
        this.oclinstancemodels = new ArrayList<>();
    }

    public gbind_simpleocl_OclMetamodel(
        String uri        ArrayList<OclInstanceModel> oclinstancemodels    ) {
        this.uri = uri;
        this.oclinstancemodels = oclinstancemodels;
    }

    public String getUri() {
        return uri;
    }

    public void setUri(String uri) {
        this.uri = uri;
    }

    public List<OclInstanceModel> getOclinstancemodels() {
        return oclinstancemodels;
    }

    public void addOclinstancemodel(Oclinstancemodel oclinstancemodel) {
        this.oclinstancemodels.add(oclinstancemodel);
    }

}