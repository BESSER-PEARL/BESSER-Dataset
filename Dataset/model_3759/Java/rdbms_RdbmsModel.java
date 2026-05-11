





import java.util.List;
import java.util.ArrayList;

public class rdbms_RdbmsModel  {

    private String version;





    private List<rdbms_RdbmsFieldType> rdbms_rdbmsfieldtypes;




    private List<rdbms_RdbmsTable> rdbms_rdbmstables;




    private List<rdbms_RdbmsView> rdbms_rdbmsviews;




    private List<rdbms_RdbmsTableOperation> rdbms_rdbmstableoperations;


    public rdbms_RdbmsModel(
        String version    ) {
        this.version = version;
        this.rdbms_rdbmsfieldtypes = new ArrayList<>();
        this.rdbms_rdbmstables = new ArrayList<>();
        this.rdbms_rdbmsviews = new ArrayList<>();
        this.rdbms_rdbmstableoperations = new ArrayList<>();
    }

    public rdbms_RdbmsModel(
        String version        ArrayList<rdbms_RdbmsFieldType> rdbms_rdbmsfieldtypes,        ArrayList<rdbms_RdbmsTable> rdbms_rdbmstables,        ArrayList<rdbms_RdbmsView> rdbms_rdbmsviews,        ArrayList<rdbms_RdbmsTableOperation> rdbms_rdbmstableoperations    ) {
        this.version = version;
        this.rdbms_rdbmsfieldtypes = rdbms_rdbmsfieldtypes;
        this.rdbms_rdbmstables = rdbms_rdbmstables;
        this.rdbms_rdbmsviews = rdbms_rdbmsviews;
        this.rdbms_rdbmstableoperations = rdbms_rdbmstableoperations;
    }

    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }

    public List<rdbms_RdbmsFieldType> getRdbms_rdbmsfieldtypes() {
        return rdbms_rdbmsfieldtypes;
    }

    public void addRdbms_rdbmsfieldtype(Rdbms_rdbmsfieldtype rdbms_rdbmsfieldtype) {
        this.rdbms_rdbmsfieldtypes.add(rdbms_rdbmsfieldtype);
    }
    public List<rdbms_RdbmsTable> getRdbms_rdbmstables() {
        return rdbms_rdbmstables;
    }

    public void addRdbms_rdbmstable(Rdbms_rdbmstable rdbms_rdbmstable) {
        this.rdbms_rdbmstables.add(rdbms_rdbmstable);
    }
    public List<rdbms_RdbmsView> getRdbms_rdbmsviews() {
        return rdbms_rdbmsviews;
    }

    public void addRdbms_rdbmsview(Rdbms_rdbmsview rdbms_rdbmsview) {
        this.rdbms_rdbmsviews.add(rdbms_rdbmsview);
    }
    public List<rdbms_RdbmsTableOperation> getRdbms_rdbmstableoperations() {
        return rdbms_rdbmstableoperations;
    }

    public void addRdbms_rdbmstableoperation(Rdbms_rdbmstableoperation rdbms_rdbmstableoperation) {
        this.rdbms_rdbmstableoperations.add(rdbms_rdbmstableoperation);
    }

}