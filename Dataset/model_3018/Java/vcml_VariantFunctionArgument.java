





import java.util.List;
import java.util.ArrayList;

public class vcml_VariantFunctionArgument  {

    private boolean in_;





    private vcml_VariantFunction vcml_variantfunction;




    private vcml_Characteristic vcml_characteristic;


    public vcml_VariantFunctionArgument(
        boolean in_    ) {
        this.in_ = in_;
    }


    public boolean getIn_() {
        return in_;
    }

    public void setIn_(boolean in_) {
        this.in_ = in_;
    }

    public vcml_VariantFunction getVcml_variantfunction() {
        return vcml_variantfunction;
    }

    public void setVcml_variantfunction(vcml_VariantFunction vcml_variantfunction) {
        this.vcml_variantfunction = vcml_variantfunction;
    }
    public vcml_Characteristic getVcml_characteristic() {
        return vcml_characteristic;
    }

    public void setVcml_characteristic(vcml_Characteristic vcml_characteristic) {
        this.vcml_characteristic = vcml_characteristic;
    }

}