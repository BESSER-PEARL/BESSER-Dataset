





import java.util.List;
import java.util.ArrayList;

public class dcmddandroid_EnumValue extends NamedElement {

    private int intValue;





    private dcmddandroid_Enum dcmddandroid_enum;


    public dcmddandroid_EnumValue(
        int intValue    ) {
        super(
        );
        this.intValue = intValue;
    }


    public int getIntvalue() {
        return intValue;
    }

    public void setIntvalue(int intValue) {
        this.intValue = intValue;
    }

    public dcmddandroid_Enum getDcmddandroid_enum() {
        return dcmddandroid_enum;
    }

    public void setDcmddandroid_enum(dcmddandroid_Enum dcmddandroid_enum) {
        this.dcmddandroid_enum = dcmddandroid_enum;
    }

}