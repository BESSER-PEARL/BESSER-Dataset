





import java.util.List;
import java.util.ArrayList;

public class smm_Characteristic extends SmmElement {

    private String name;





    private smm_Characteristic smm_characteristic;


    public smm_Characteristic(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public smm_Characteristic getSmm_characteristic() {
        return smm_characteristic;
    }

    public void setSmm_characteristic(smm_Characteristic smm_characteristic) {
        this.smm_characteristic = smm_characteristic;
    }

}