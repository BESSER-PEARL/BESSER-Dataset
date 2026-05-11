





import java.util.List;
import java.util.ArrayList;

public class vcml_ObjectCharacteristicReference extends CharacteristicReference_C {






    private vcml_ConstraintObject vcml_constraintobject;




    private vcml_Characteristic vcml_characteristic;


    public vcml_ObjectCharacteristicReference(
    ) {
        super(
        );
    }



    public vcml_ConstraintObject getVcml_constraintobject() {
        return vcml_constraintobject;
    }

    public void setVcml_constraintobject(vcml_ConstraintObject vcml_constraintobject) {
        this.vcml_constraintobject = vcml_constraintobject;
    }
    public vcml_Characteristic getVcml_characteristic() {
        return vcml_characteristic;
    }

    public void setVcml_characteristic(vcml_Characteristic vcml_characteristic) {
        this.vcml_characteristic = vcml_characteristic;
    }

}