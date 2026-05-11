





import java.util.List;
import java.util.ArrayList;

public class sxfm_Data  {

    private String name;
    private String value;





    private sxfm_MetadataSet sxfm_metadataset;


    public sxfm_Data(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public sxfm_MetadataSet getSxfm_metadataset() {
        return sxfm_metadataset;
    }

    public void setSxfm_metadataset(sxfm_MetadataSet sxfm_metadataset) {
        this.sxfm_metadataset = sxfm_metadataset;
    }

}