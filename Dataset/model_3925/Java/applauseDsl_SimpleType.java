





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_SimpleType extends Type {

    private String platformType;



    public applauseDsl_SimpleType(
        String platformType    ) {
        super(
        );
        this.platformType = platformType;
    }


    public String getPlatformtype() {
        return platformType;
    }

    public void setPlatformtype(String platformType) {
        this.platformType = platformType;
    }


}