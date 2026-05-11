





import java.util.List;
import java.util.ArrayList;

public class avm_Container  {

    private String Name;
    private String YPosition;
    private String XPosition;
    private String ID;
    private String Description;
    private String Classifications;





    private avm_Design avm_design;




    private List<avm_Port> avm_ports;




    private List<avm_Connector> avm_connectors;




    private avm_Container avm_container;


    public avm_Container(
        String Name,        String YPosition,        String XPosition,        String ID,        String Description,        String Classifications    ) {
        this.Name = Name;
        this.YPosition = YPosition;
        this.XPosition = XPosition;
        this.ID = ID;
        this.Description = Description;
        this.Classifications = Classifications;
        this.avm_ports = new ArrayList<>();
        this.avm_connectors = new ArrayList<>();
    }

    public avm_Container(
        String Name,        String YPosition,        String XPosition,        String ID,        String Description,        String Classifications        ArrayList<avm_Port> avm_ports,        ArrayList<avm_Connector> avm_connectors    ) {
        this.Name = Name;
        this.YPosition = YPosition;
        this.XPosition = XPosition;
        this.ID = ID;
        this.Description = Description;
        this.Classifications = Classifications;
        this.avm_ports = avm_ports;
        this.avm_connectors = avm_connectors;
    }

    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }
    public String getYposition() {
        return YPosition;
    }

    public void setYposition(String YPosition) {
        this.YPosition = YPosition;
    }
    public String getXposition() {
        return XPosition;
    }

    public void setXposition(String XPosition) {
        this.XPosition = XPosition;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getClassifications() {
        return Classifications;
    }

    public void setClassifications(String Classifications) {
        this.Classifications = Classifications;
    }

    public avm_Design getAvm_design() {
        return avm_design;
    }

    public void setAvm_design(avm_Design avm_design) {
        this.avm_design = avm_design;
    }
    public List<avm_Port> getAvm_ports() {
        return avm_ports;
    }

    public void addAvm_port(Avm_port avm_port) {
        this.avm_ports.add(avm_port);
    }
    public List<avm_Connector> getAvm_connectors() {
        return avm_connectors;
    }

    public void addAvm_connector(Avm_connector avm_connector) {
        this.avm_connectors.add(avm_connector);
    }
    public avm_Container getAvm_container() {
        return avm_container;
    }

    public void setAvm_container(avm_Container avm_container) {
        this.avm_container = avm_container;
    }

}