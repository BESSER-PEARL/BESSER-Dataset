





import java.util.List;
import java.util.ArrayList;

public class sadl_RangeType  {

    private String dataType;





    private sadl_ResourceIdentifier sadl_resourceidentifier;




    private sadl_Range sadl_range;


    public sadl_RangeType(
        String dataType    ) {
        this.dataType = dataType;
    }


    public String getDatatype() {
        return dataType;
    }

    public void setDatatype(String dataType) {
        this.dataType = dataType;
    }

    public sadl_ResourceIdentifier getSadl_resourceidentifier() {
        return sadl_resourceidentifier;
    }

    public void setSadl_resourceidentifier(sadl_ResourceIdentifier sadl_resourceidentifier) {
        this.sadl_resourceidentifier = sadl_resourceidentifier;
    }
    public sadl_Range getSadl_range() {
        return sadl_range;
    }

    public void setSadl_range(sadl_Range sadl_range) {
        this.sadl_range = sadl_range;
    }

}