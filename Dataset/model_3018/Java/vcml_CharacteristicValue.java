





import java.util.List;
import java.util.ArrayList;

public class vcml_CharacteristicValue  {

    private boolean default;
    private String name;





    private vcml_Documentation vcml_documentation;




    private vcml_Description vcml_description;




    private vcml_CharacteristicOrValueDependencies vcml_characteristicorvaluedependencies;




    private vcml_SymbolicType vcml_symbolictype;


    public vcml_CharacteristicValue(
        boolean default,        String name    ) {
        this.default = default;
        this.name = name;
    }


    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vcml_Documentation getVcml_documentation() {
        return vcml_documentation;
    }

    public void setVcml_documentation(vcml_Documentation vcml_documentation) {
        this.vcml_documentation = vcml_documentation;
    }
    public vcml_Description getVcml_description() {
        return vcml_description;
    }

    public void setVcml_description(vcml_Description vcml_description) {
        this.vcml_description = vcml_description;
    }
    public vcml_CharacteristicOrValueDependencies getVcml_characteristicorvaluedependencies() {
        return vcml_characteristicorvaluedependencies;
    }

    public void setVcml_characteristicorvaluedependencies(vcml_CharacteristicOrValueDependencies vcml_characteristicorvaluedependencies) {
        this.vcml_characteristicorvaluedependencies = vcml_characteristicorvaluedependencies;
    }
    public vcml_SymbolicType getVcml_symbolictype() {
        return vcml_symbolictype;
    }

    public void setVcml_symbolictype(vcml_SymbolicType vcml_symbolictype) {
        this.vcml_symbolictype = vcml_symbolictype;
    }

}