





import java.util.List;
import java.util.ArrayList;

public class express_core_ExplicitAttribute extends Attribute {

    private String isOptional;



    public express_core_ExplicitAttribute(
        String isOptional    ) {
        super(
        );
        this.isOptional = isOptional;
    }


    public String getIsoptional() {
        return isOptional;
    }

    public void setIsoptional(String isOptional) {
        this.isOptional = isOptional;
    }


}