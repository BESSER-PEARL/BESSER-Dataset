





import java.util.List;
import java.util.ArrayList;

public class vcml_NumericCharacteristicValue  {

    private boolean default;





    private vcml_Documentation vcml_documentation;




    private vcml_CharacteristicOrValueDependencies vcml_characteristicorvaluedependencies;




    private vcml_NumericType vcml_numerictype;


    public vcml_NumericCharacteristicValue(
        boolean default    ) {
        this.default = default;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }

    public vcml_Documentation getVcml_documentation() {
        return vcml_documentation;
    }

    public void setVcml_documentation(vcml_Documentation vcml_documentation) {
        this.vcml_documentation = vcml_documentation;
    }
    public vcml_CharacteristicOrValueDependencies getVcml_characteristicorvaluedependencies() {
        return vcml_characteristicorvaluedependencies;
    }

    public void setVcml_characteristicorvaluedependencies(vcml_CharacteristicOrValueDependencies vcml_characteristicorvaluedependencies) {
        this.vcml_characteristicorvaluedependencies = vcml_characteristicorvaluedependencies;
    }
    public vcml_NumericType getVcml_numerictype() {
        return vcml_numerictype;
    }

    public void setVcml_numerictype(vcml_NumericType vcml_numerictype) {
        this.vcml_numerictype = vcml_numerictype;
    }

}