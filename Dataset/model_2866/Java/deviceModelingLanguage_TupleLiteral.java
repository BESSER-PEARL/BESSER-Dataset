





import java.util.List;
import java.util.ArrayList;

public class deviceModelingLanguage_TupleLiteral extends Literal {






    private List<deviceModelingLanguage_Literal> devicemodelinglanguage_literals;


    public deviceModelingLanguage_TupleLiteral(
    ) {
        super(
        );
        this.devicemodelinglanguage_literals = new ArrayList<>();
    }

    public deviceModelingLanguage_TupleLiteral(
        ArrayList<deviceModelingLanguage_Literal> devicemodelinglanguage_literals    ) {
        this.devicemodelinglanguage_literals = devicemodelinglanguage_literals;
    }


    public List<deviceModelingLanguage_Literal> getDevicemodelinglanguage_literals() {
        return devicemodelinglanguage_literals;
    }

    public void addDevicemodelinglanguage_literal(Devicemodelinglanguage_literal devicemodelinglanguage_literal) {
        this.devicemodelinglanguage_literals.add(devicemodelinglanguage_literal);
    }

}