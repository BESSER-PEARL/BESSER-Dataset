





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_SimpleSetLiteral extends SimpleLiteral {






    private List<deviceModelingLanguage_SimpleLiteral> devicemodelinglanguage_simpleliterals;


    public deviceModelingLanguage_SimpleSetLiteral(
    ) {
        super(
        );
        this.devicemodelinglanguage_simpleliterals = new ArrayList<>();
    }

    public deviceModelingLanguage_SimpleSetLiteral(
        ArrayList<deviceModelingLanguage_SimpleLiteral> devicemodelinglanguage_simpleliterals    ) {
        this.devicemodelinglanguage_simpleliterals = devicemodelinglanguage_simpleliterals;
    }


    public List<deviceModelingLanguage_SimpleLiteral> getDevicemodelinglanguage_simpleliterals() {
        return devicemodelinglanguage_simpleliterals;
    }

    public void addDevicemodelinglanguage_simpleliteral(Devicemodelinglanguage_simpleliteral devicemodelinglanguage_simpleliteral) {
        this.devicemodelinglanguage_simpleliterals.add(devicemodelinglanguage_simpleliteral);
    }

}