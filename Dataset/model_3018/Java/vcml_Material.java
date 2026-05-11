





import java.util.List;
import java.util.ArrayList;

public class vcml_Material extends VCObject {

    private String type;





    private List<vcml_BillOfMaterial> vcml_billofmaterials;




    private vcml_BillOfMaterial vcml_billofmaterial;


    public vcml_Material(
        String type    ) {
        super(
        );
        this.type = type;
        this.vcml_billofmaterials = new ArrayList<>();
    }

    public vcml_Material(
        String type        ArrayList<vcml_BillOfMaterial> vcml_billofmaterials    ) {
        this.type = type;
        this.vcml_billofmaterials = vcml_billofmaterials;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public List<vcml_BillOfMaterial> getVcml_billofmaterials() {
        return vcml_billofmaterials;
    }

    public void addVcml_billofmaterial(Vcml_billofmaterial vcml_billofmaterial) {
        this.vcml_billofmaterials.add(vcml_billofmaterial);
    }
    public vcml_BillOfMaterial getVcml_billofmaterial() {
        return vcml_billofmaterial;
    }

    public void setVcml_billofmaterial(vcml_BillOfMaterial vcml_billofmaterial) {
        this.vcml_billofmaterial = vcml_billofmaterial;
    }

}