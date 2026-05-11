





import java.util.List;
import java.util.ArrayList;

public class vcml_ConfigurationProfile extends VCObject {

    private String bomapplication;
    private String status;
    private String fixing;





    private List<vcml_DependencyNet> vcml_dependencynets;




    private vcml_InterfaceDesign vcml_interfacedesign;




    private vcml_Material vcml_material;




    private vcml_Material vcml_material;


    public vcml_ConfigurationProfile(
        String bomapplication,        String status,        String fixing    ) {
        super(
        );
        this.bomapplication = bomapplication;
        this.status = status;
        this.fixing = fixing;
        this.vcml_dependencynets = new ArrayList<>();
    }

    public vcml_ConfigurationProfile(
        String bomapplication,        String status,        String fixing        ArrayList<vcml_DependencyNet> vcml_dependencynets    ) {
        this.bomapplication = bomapplication;
        this.status = status;
        this.fixing = fixing;
        this.vcml_dependencynets = vcml_dependencynets;
    }

    public String getBomapplication() {
        return bomapplication;
    }

    public void setBomapplication(String bomapplication) {
        this.bomapplication = bomapplication;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getFixing() {
        return fixing;
    }

    public void setFixing(String fixing) {
        this.fixing = fixing;
    }

    public List<vcml_DependencyNet> getVcml_dependencynets() {
        return vcml_dependencynets;
    }

    public void addVcml_dependencynet(Vcml_dependencynet vcml_dependencynet) {
        this.vcml_dependencynets.add(vcml_dependencynet);
    }
    public vcml_InterfaceDesign getVcml_interfacedesign() {
        return vcml_interfacedesign;
    }

    public void setVcml_interfacedesign(vcml_InterfaceDesign vcml_interfacedesign) {
        this.vcml_interfacedesign = vcml_interfacedesign;
    }
    public vcml_Material getVcml_material() {
        return vcml_material;
    }

    public void setVcml_material(vcml_Material vcml_material) {
        this.vcml_material = vcml_material;
    }
    public vcml_Material getVcml_material() {
        return vcml_material;
    }

    public void setVcml_material(vcml_Material vcml_material) {
        this.vcml_material = vcml_material;
    }

}