





import java.util.List;
import java.util.ArrayList;

public class columnFamilyDataModel_SimpleType extends Type {

    private String type;



    public columnFamilyDataModel_SimpleType(
        String type    ) {
        super(
        );
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}