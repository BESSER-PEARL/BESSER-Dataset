





import java.util.List;
import java.util.ArrayList;

public class domainmodel_BindEnumSource extends BindSource {

    private String enumType;



    public domainmodel_BindEnumSource(
        String enumType    ) {
        super(
        );
        this.enumType = enumType;
    }


    public String getEnumtype() {
        return enumType;
    }

    public void setEnumtype(String enumType) {
        this.enumType = enumType;
    }


}