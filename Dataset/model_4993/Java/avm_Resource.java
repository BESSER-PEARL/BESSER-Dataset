





import java.util.List;
import java.util.ArrayList;

public class avm_Resource  {

    private String Hash;
    private String Name;
    private String ID;
    private String XPosition;
    private String Notes;
    private String YPosition;
    private String Path;





    private avm_Component avm_component;




    private avm_DataSource avm_datasource;




    private avm_DomainModel_ avm_domainmodel_;




    private avm_Container avm_container;




    private avm_Container avm_container;




    private avm_Design avm_design;


    public avm_Resource(
        String Hash,        String Name,        String ID,        String XPosition,        String Notes,        String YPosition,        String Path    ) {
        this.Hash = Hash;
        this.Name = Name;
        this.ID = ID;
        this.XPosition = XPosition;
        this.Notes = Notes;
        this.YPosition = YPosition;
        this.Path = Path;
    }


    public String getHash() {
        return Hash;
    }

    public void setHash(String Hash) {
        this.Hash = Hash;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getNotes() {
        return Notes;
    }

    public void setNotes(String Notes) {
        this.Notes = Notes;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getPath() {
        return Path;
    }

    public void setPath(String Path) {
        this.Path = Path;
    }

    public avm_Component getAvm_component() {
        return avm_component;
    }

    public void setAvm_component(avm_Component avm_component) {
        this.avm_component = avm_component;
    }
    public avm_DataSource getAvm_datasource() {
        return avm_datasource;
    }

    public void setAvm_datasource(avm_DataSource avm_datasource) {
        this.avm_datasource = avm_datasource;
    }
    public avm_DomainModel_ getAvm_domainmodel_() {
        return avm_domainmodel_;
    }

    public void setAvm_domainmodel_(avm_DomainModel_ avm_domainmodel_) {
        this.avm_domainmodel_ = avm_domainmodel_;
    }
    public avm_Container getAvm_container() {
        return avm_container;
    }

    public void setAvm_container(avm_Container avm_container) {
        this.avm_container = avm_container;
    }
    public avm_Container getAvm_container() {
        return avm_container;
    }

    public void setAvm_container(avm_Container avm_container) {
        this.avm_container = avm_container;
    }
    public avm_Design getAvm_design() {
        return avm_design;
    }

    public void setAvm_design(avm_Design avm_design) {
        this.avm_design = avm_design;
    }

}