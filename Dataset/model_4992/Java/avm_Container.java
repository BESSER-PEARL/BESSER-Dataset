





import java.util.List;
import java.util.ArrayList;

public class avm_Container  {

    private String YPosition;
    private String XPosition;
    private String Description;
    private String ID;
    private String Name;





    private List<avm_Resource> avm_resources;




    private List<avm_ComponentInstance> avm_componentinstances;




    private List<avm_Resource> avm_resources;




    private List<avm_Property> avm_propertys;




    private List<avm_Connector> avm_connectors;




    private avm_Container avm_container;




    private List<avm_Formula> avm_formulas;




    private avm_Design avm_design;




    private List<avm_assemblyDetail> avm_assemblydetails;




    private List<avm_Port> avm_ports;




    private List<avm_DomainModel_> avm_domainmodel_s;




    private List<avm_ContainerFeature> avm_containerfeatures;


    public avm_Container(
        String YPosition,        String XPosition,        String Description,        String ID,        String Name    ) {
        this.YPosition = YPosition;
        this.XPosition = XPosition;
        this.Description = Description;
        this.ID = ID;
        this.Name = Name;
        this.avm_resources = new ArrayList<>();
        this.avm_componentinstances = new ArrayList<>();
        this.avm_resources = new ArrayList<>();
        this.avm_propertys = new ArrayList<>();
        this.avm_connectors = new ArrayList<>();
        this.avm_formulas = new ArrayList<>();
        this.avm_assemblydetails = new ArrayList<>();
        this.avm_ports = new ArrayList<>();
        this.avm_domainmodel_s = new ArrayList<>();
        this.avm_containerfeatures = new ArrayList<>();
    }

    public avm_Container(
        String YPosition,        String XPosition,        String Description,        String ID,        String Name        ArrayList<avm_Resource> avm_resources,        ArrayList<avm_ComponentInstance> avm_componentinstances,        ArrayList<avm_Resource> avm_resources,        ArrayList<avm_Property> avm_propertys,        ArrayList<avm_Connector> avm_connectors,        ArrayList<avm_Formula> avm_formulas,        ArrayList<avm_assemblyDetail> avm_assemblydetails,        ArrayList<avm_Port> avm_ports,        ArrayList<avm_DomainModel_> avm_domainmodel_s,        ArrayList<avm_ContainerFeature> avm_containerfeatures    ) {
        this.YPosition = YPosition;
        this.XPosition = XPosition;
        this.Description = Description;
        this.ID = ID;
        this.Name = Name;
        this.avm_resources = avm_resources;
        this.avm_componentinstances = avm_componentinstances;
        this.avm_resources = avm_resources;
        this.avm_propertys = avm_propertys;
        this.avm_connectors = avm_connectors;
        this.avm_formulas = avm_formulas;
        this.avm_assemblydetails = avm_assemblydetails;
        this.avm_ports = avm_ports;
        this.avm_domainmodel_s = avm_domainmodel_s;
        this.avm_containerfeatures = avm_containerfeatures;
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
    public String getDescription() {
        return Description;
    }

    public void setDescription(String Description) {
        this.Description = Description;
    }
    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }

    public List<avm_Resource> getAvm_resources() {
        return avm_resources;
    }

    public void addAvm_resource(Avm_resource avm_resource) {
        this.avm_resources.add(avm_resource);
    }
    public List<avm_ComponentInstance> getAvm_componentinstances() {
        return avm_componentinstances;
    }

    public void addAvm_componentinstance(Avm_componentinstance avm_componentinstance) {
        this.avm_componentinstances.add(avm_componentinstance);
    }
    public List<avm_Resource> getAvm_resources() {
        return avm_resources;
    }

    public void addAvm_resource(Avm_resource avm_resource) {
        this.avm_resources.add(avm_resource);
    }
    public List<avm_Property> getAvm_propertys() {
        return avm_propertys;
    }

    public void addAvm_property(Avm_property avm_property) {
        this.avm_propertys.add(avm_property);
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
    public List<avm_Formula> getAvm_formulas() {
        return avm_formulas;
    }

    public void addAvm_formula(Avm_formula avm_formula) {
        this.avm_formulas.add(avm_formula);
    }
    public avm_Design getAvm_design() {
        return avm_design;
    }

    public void setAvm_design(avm_Design avm_design) {
        this.avm_design = avm_design;
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
    public List<avm_DomainModel_> getAvm_domainmodel_s() {
        return avm_domainmodel_s;
    }

    public void addAvm_domainmodel_(Avm_domainmodel_ avm_domainmodel_) {
        this.avm_domainmodel_s.add(avm_domainmodel_);
    }
    public List<avm_ContainerFeature> getAvm_containerfeatures() {
        return avm_containerfeatures;
    }

    public void addAvm_containerfeature(Avm_containerfeature avm_containerfeature) {
        this.avm_containerfeatures.add(avm_containerfeature);
    }

}