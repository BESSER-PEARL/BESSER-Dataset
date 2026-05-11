





import java.util.List;
import java.util.ArrayList;

public class vcml_CharacteristicReference_P extends Literal {

    private String location;





    private vcml_MDataCharacteristic_P vcml_mdatacharacteristic_p;




    private vcml_Characteristic vcml_characteristic;




    private vcml_IsSpecified_P vcml_isspecified_p;




    private vcml_InCondition_P vcml_incondition_p;


    public vcml_CharacteristicReference_P(
        String location    ) {
        super(
        );
        this.location = location;
    }


    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }

    public vcml_MDataCharacteristic_P getVcml_mdatacharacteristic_p() {
        return vcml_mdatacharacteristic_p;
    }

    public void setVcml_mdatacharacteristic_p(vcml_MDataCharacteristic_P vcml_mdatacharacteristic_p) {
        this.vcml_mdatacharacteristic_p = vcml_mdatacharacteristic_p;
    }
    public vcml_Characteristic getVcml_characteristic() {
        return vcml_characteristic;
    }

    public void setVcml_characteristic(vcml_Characteristic vcml_characteristic) {
        this.vcml_characteristic = vcml_characteristic;
    }
    public vcml_IsSpecified_P getVcml_isspecified_p() {
        return vcml_isspecified_p;
    }

    public void setVcml_isspecified_p(vcml_IsSpecified_P vcml_isspecified_p) {
        this.vcml_isspecified_p = vcml_isspecified_p;
    }
    public vcml_InCondition_P getVcml_incondition_p() {
        return vcml_incondition_p;
    }

    public void setVcml_incondition_p(vcml_InCondition_P vcml_incondition_p) {
        this.vcml_incondition_p = vcml_incondition_p;
    }

}