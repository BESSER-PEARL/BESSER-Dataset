





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_TupleType extends BaseType {






    private List<deviceModelingLanguage_Type> devicemodelinglanguage_types;


    public deviceModelingLanguage_TupleType(
    ) {
        super(
        );
        this.devicemodelinglanguage_types = new ArrayList<>();
    }

    public deviceModelingLanguage_TupleType(
        ArrayList<deviceModelingLanguage_Type> devicemodelinglanguage_types    ) {
        this.devicemodelinglanguage_types = devicemodelinglanguage_types;
    }


    public List<deviceModelingLanguage_Type> getDevicemodelinglanguage_types() {
        return devicemodelinglanguage_types;
    }

    public void addDevicemodelinglanguage_type(Devicemodelinglanguage_type devicemodelinglanguage_type) {
        this.devicemodelinglanguage_types.add(devicemodelinglanguage_type);
    }

}