





import java.util.List;
import java.util.ArrayList;

public class avm_Container  {

    private String YPosition;
    private String XPosition;
    private String Name;





    private List<avm_Property> avm_propertys;




    private List<avm_Formula> avm_formulas;




    private List<avm_Connector> avm_connectors;




    private List<avm_Container> avm_containers;




    private List<avm_assemblyDetail> avm_assemblydetails;




    private List<avm_Port> avm_ports;




    private List<avm_ComponentInstance> avm_componentinstances;




    private avm_Design avm_design;


    public avm_Container(
        String YPosition,        String XPosition,        String Name    ) {
        this.YPosition = YPosition;
        this.XPosition = XPosition;
        this.Name = Name;
        this.avm_propertys = new ArrayList<>();
        this.avm_formulas = new ArrayList<>();
        this.avm_connectors = new ArrayList<>();
        this.avm_containers = new ArrayList<>();
        this.avm_assemblydetails = new ArrayList<>();
        this.avm_ports = new ArrayList<>();
        this.avm_componentinstances = new ArrayList<>();
    }

    public avm_Container(
        String YPosition,        String XPosition,        String Name        ArrayList<avm_Property> avm_propertys,        ArrayList<avm_Formula> avm_formulas,        ArrayList<avm_Connector> avm_connectors,        ArrayList<avm_Container> avm_containers,        ArrayList<avm_assemblyDetail> avm_assemblydetails,        ArrayList<avm_Port> avm_ports,        ArrayList<avm_ComponentInstance> avm_componentinstances    ) {
        this.YPosition = YPosition;
        this.XPosition = XPosition;
        this.Name = Name;
        this.avm_propertys = avm_propertys;
        this.avm_formulas = avm_formulas;
        this.avm_connectors = avm_connectors;
        this.avm_containers = avm_containers;
        this.avm_assemblydetails = avm_assemblydetails;
        this.avm_ports = avm_ports;
        this.avm_componentinstances = avm_componentinstances;
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
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<avm_Property> getAvm_propertys() {
        return avm_propertys;
    }

    public void addAvm_property(Avm_property avm_property) {
        this.avm_propertys.add(avm_property);
    }
    public List<avm_Formula> getAvm_formulas() {
        return avm_formulas;
    }

    public void addAvm_formula(Avm_formula avm_formula) {
        this.avm_formulas.add(avm_formula);
    }
    public List<avm_Connector> getAvm_connectors() {
        return avm_connectors;
    }

    public void addAvm_connector(Avm_connector avm_connector) {
        this.avm_connectors.add(avm_connector);
    }
    public List<avm_Container> getAvm_containers() {
        return avm_containers;
    }

    public void addAvm_container(Avm_container avm_container) {
        this.avm_containers.add(avm_container);
    }
    public List<avm_assemblyDetail> getAvm_assemblydetails() {
        return avm_assemblydetails;
    }

    public void addAvm_assemblydetail(Avm_assemblydetail avm_assemblydetail) {
        this.avm_assemblydetails.add(avm_assemblydetail);
    }
    public List<avm_Port> getAvm_ports() {
        return avm_ports;
    }

    public void addAvm_port(Avm_port avm_port) {
        this.avm_ports.add(avm_port);
    }
    public List<avm_ComponentInstance> getAvm_componentinstances() {
        return avm_componentinstances;
    }

    public void addAvm_componentinstance(Avm_componentinstance avm_componentinstance) {
        this.avm_componentinstances.add(avm_componentinstance);
    }
    public avm_Design getAvm_design() {
        return avm_design;
    }

    public void setAvm_design(avm_Design avm_design) {
        this.avm_design = avm_design;
    }

}