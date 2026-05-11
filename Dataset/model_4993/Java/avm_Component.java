





import java.util.List;
import java.util.ArrayList;

public class avm_Component  {

    private String Name;
    private String Supercedes;
    private String Classifications;
    private String Version;
    private String ID;
    private String SchemaVersion;





    private List<avm_Connector> avm_connectors;




    private List<avm_Port> avm_ports;




    private List<avm_Property> avm_propertys;


    public avm_Component(
        String Name,        String Supercedes,        String Classifications,        String Version,        String ID,        String SchemaVersion    ) {
        this.Name = Name;
        this.Supercedes = Supercedes;
        this.Classifications = Classifications;
        this.Version = Version;
        this.ID = ID;
        this.SchemaVersion = SchemaVersion;
        this.avm_connectors = new ArrayList<>();
        this.avm_ports = new ArrayList<>();
        this.avm_propertys = new ArrayList<>();
    }

    public avm_Component(
        String Name,        String Supercedes,        String Classifications,        String Version,        String ID,        String SchemaVersion        ArrayList<avm_Connector> avm_connectors,        ArrayList<avm_Port> avm_ports,        ArrayList<avm_Property> avm_propertys    ) {
        this.Name = Name;
        this.Supercedes = Supercedes;
        this.Classifications = Classifications;
        this.Version = Version;
        this.ID = ID;
        this.SchemaVersion = SchemaVersion;
        this.avm_connectors = avm_connectors;
        this.avm_ports = avm_ports;
        this.avm_propertys = avm_propertys;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getSupercedes() {
        return Supercedes;
    }

    public void setSupercedes(String Supercedes) {
        this.Supercedes = Supercedes;
    }
    public String getClassifications() {
        return Classifications;
    }

    public void setClassifications(String Classifications) {
        this.Classifications = Classifications;
    }
    public String getVersion() {
        return Version;
    }

    public void setVersion(String Version) {
        this.Version = Version;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getSchemaversion() {
        return SchemaVersion;
    }

    public void setSchemaversion(String SchemaVersion) {
        this.SchemaVersion = SchemaVersion;
    }

    public List<avm_Connector> getAvm_connectors() {
        return avm_connectors;
    }

    public void addAvm_connector(Avm_connector avm_connector) {
        this.avm_connectors.add(avm_connector);
    }
    public List<avm_Port> getAvm_ports() {
        return avm_ports;
    }

    public void addAvm_port(Avm_port avm_port) {
        this.avm_ports.add(avm_port);
    }
    public List<avm_Property> getAvm_propertys() {
        return avm_propertys;
    }

    public void addAvm_property(Avm_property avm_property) {
        this.avm_propertys.add(avm_property);
    }

}