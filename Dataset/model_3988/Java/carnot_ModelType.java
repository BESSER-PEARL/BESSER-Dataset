





import java.util.List;
import java.util.ArrayList;

public class carnot_ModelType extends IIdentifiableElement, IExtensibleElement {

    private String oid;
    private String created;
    private String vendor;
    private String author;
    private String modelOID;
    private String carnotVersion;





    private List<carnot_DiagramType> carnot_diagramtypes;




    private List<carnot_ViewType> carnot_viewtypes;


    public carnot_ModelType(
        String oid,        String created,        String vendor,        String author,        String modelOID,        String carnotVersion    ) {
        super(
        );
        this.oid = oid;
        this.created = created;
        this.vendor = vendor;
        this.author = author;
        this.modelOID = modelOID;
        this.carnotVersion = carnotVersion;
        this.carnot_diagramtypes = new ArrayList<>();
        this.carnot_viewtypes = new ArrayList<>();
    }

    public carnot_ModelType(
        String oid,        String created,        String vendor,        String author,        String modelOID,        String carnotVersion        ArrayList<carnot_DiagramType> carnot_diagramtypes,        ArrayList<carnot_ViewType> carnot_viewtypes    ) {
        this.oid = oid;
        this.created = created;
        this.vendor = vendor;
        this.author = author;
        this.modelOID = modelOID;
        this.carnotVersion = carnotVersion;
        this.carnot_diagramtypes = carnot_diagramtypes;
        this.carnot_viewtypes = carnot_viewtypes;
    }

    public String getOid() {
        return oid;
    }

    public void setOid(String oid) {
        this.oid = oid;
    }
    public String getCreated() {
        return created;
    }

    public void setCreated(String created) {
        this.created = created;
    }
    public String getVendor() {
        return vendor;
    }

    public void setVendor(String vendor) {
        this.vendor = vendor;
    }
    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }
    public String getModeloid() {
        return modelOID;
    }

    public void setModeloid(String modelOID) {
        this.modelOID = modelOID;
    }
    public String getCarnotversion() {
        return carnotVersion;
    }

    public void setCarnotversion(String carnotVersion) {
        this.carnotVersion = carnotVersion;
    }

    public List<carnot_DiagramType> getCarnot_diagramtypes() {
        return carnot_diagramtypes;
    }

    public void addCarnot_diagramtype(Carnot_diagramtype carnot_diagramtype) {
        this.carnot_diagramtypes.add(carnot_diagramtype);
    }
    public List<carnot_ViewType> getCarnot_viewtypes() {
        return carnot_viewtypes;
    }

    public void addCarnot_viewtype(Carnot_viewtype carnot_viewtype) {
        this.carnot_viewtypes.add(carnot_viewtype);
    }

}