





import java.util.List;
import java.util.ArrayList;

public class vcml_CharacteristicType  {

    private int numberOfChars;





    private vcml_Characteristic vcml_characteristic;


    public vcml_CharacteristicType(
        int numberOfChars    ) {
        this.numberOfChars = numberOfChars;
    }


    public int getNumberofchars() {
        return numberOfChars;
    }

    public void setNumberofchars(int numberOfChars) {
        this.numberOfChars = numberOfChars;
    }

    public vcml_Characteristic getVcml_characteristic() {
        return vcml_characteristic;
    }

    public void setVcml_characteristic(vcml_Characteristic vcml_characteristic) {
        this.vcml_characteristic = vcml_characteristic;
    }

}