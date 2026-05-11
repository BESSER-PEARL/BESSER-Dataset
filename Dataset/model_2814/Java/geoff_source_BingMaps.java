





import java.util.List;
import java.util.ArrayList;

public class geoff_source_BingMaps extends XYZ {

    private String key;
    private String imagerySet;



    public geoff_source_BingMaps(
        String key,        String imagerySet    ) {
        super(
        );
        this.key = key;
        this.imagerySet = imagerySet;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getImageryset() {
        return imagerySet;
    }

    public void setImageryset(String imagerySet) {
        this.imagerySet = imagerySet;
    }


}