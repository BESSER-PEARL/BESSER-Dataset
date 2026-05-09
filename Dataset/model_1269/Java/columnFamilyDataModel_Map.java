





import java.util.List;
import java.util.ArrayList;

public class columnFamilyDataModel_Map extends Collection {

    private String keyType;



    public columnFamilyDataModel_Map(
        String keyType    ) {
        super(
        );
        this.keyType = keyType;
    }


    public String getKeytype() {
        return keyType;
    }

    public void setKeytype(String keyType) {
        this.keyType = keyType;
    }


}