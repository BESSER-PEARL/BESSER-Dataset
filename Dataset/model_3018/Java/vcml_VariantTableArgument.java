





import java.util.List;
import java.util.ArrayList;

public class vcml_VariantTableArgument  {

    private boolean key;





    private vcml_VariantTable vcml_varianttable;




    private vcml_Characteristic vcml_characteristic;


    public vcml_VariantTableArgument(
        boolean key    ) {
        this.key = key;
    }


    public boolean getKey() {
        return key;
    }

    public void setKey(boolean key) {
        this.key = key;
    }

    public vcml_VariantTable getVcml_varianttable() {
        return vcml_varianttable;
    }

    public void setVcml_varianttable(vcml_VariantTable vcml_varianttable) {
        this.vcml_varianttable = vcml_varianttable;
    }
    public vcml_Characteristic getVcml_characteristic() {
        return vcml_characteristic;
    }

    public void setVcml_characteristic(vcml_Characteristic vcml_characteristic) {
        this.vcml_characteristic = vcml_characteristic;
    }

}