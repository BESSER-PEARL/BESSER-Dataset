





import java.util.List;
import java.util.ArrayList;

public class vcml_CharacteristicGroup  {

    private String name;





    private vcml_InterfaceDesign vcml_interfacedesign;




    private vcml_Description vcml_description;




    private List<vcml_Characteristic> vcml_characteristics;


    public vcml_CharacteristicGroup(
        String name    ) {
        this.name = name;
        this.vcml_characteristics = new ArrayList<>();
    }

    public vcml_CharacteristicGroup(
        String name        ArrayList<vcml_Characteristic> vcml_characteristics    ) {
        this.name = name;
        this.vcml_characteristics = vcml_characteristics;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vcml_InterfaceDesign getVcml_interfacedesign() {
        return vcml_interfacedesign;
    }

    public void setVcml_interfacedesign(vcml_InterfaceDesign vcml_interfacedesign) {
        this.vcml_interfacedesign = vcml_interfacedesign;
    }
    public vcml_Description getVcml_description() {
        return vcml_description;
    }

    public void setVcml_description(vcml_Description vcml_description) {
        this.vcml_description = vcml_description;
    }
    public List<vcml_Characteristic> getVcml_characteristics() {
        return vcml_characteristics;
    }

    public void addVcml_characteristic(Vcml_characteristic vcml_characteristic) {
        this.vcml_characteristics.add(vcml_characteristic);
    }

}