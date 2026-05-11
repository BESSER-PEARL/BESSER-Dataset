





import java.util.List;
import java.util.ArrayList;

public class vcml_DateCharacteristicValue  {

    private String to;
    private boolean default;
    private String from_;





    private vcml_CharacteristicOrValueDependencies vcml_characteristicorvaluedependencies;




    private vcml_Documentation vcml_documentation;




    private vcml_DateType vcml_datetype;


    public vcml_DateCharacteristicValue(
        String to,        boolean default,        String from_    ) {
        this.to = to;
        this.default = default;
        this.from_ = from_;
    }


    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }

    public vcml_CharacteristicOrValueDependencies getVcml_characteristicorvaluedependencies() {
        return vcml_characteristicorvaluedependencies;
    }

    public void setVcml_characteristicorvaluedependencies(vcml_CharacteristicOrValueDependencies vcml_characteristicorvaluedependencies) {
        this.vcml_characteristicorvaluedependencies = vcml_characteristicorvaluedependencies;
    }
    public vcml_Documentation getVcml_documentation() {
        return vcml_documentation;
    }

    public void setVcml_documentation(vcml_Documentation vcml_documentation) {
        this.vcml_documentation = vcml_documentation;
    }
    public vcml_DateType getVcml_datetype() {
        return vcml_datetype;
    }

    public void setVcml_datetype(vcml_DateType vcml_datetype) {
        this.vcml_datetype = vcml_datetype;
    }

}