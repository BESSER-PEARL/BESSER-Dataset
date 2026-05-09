





import java.util.List;
import java.util.ArrayList;

public class model_values_Metadata extends MetadataValue {






    private List<StringToValueMap> stringtovaluemaps;


    public model_values_Metadata(
    ) {
        super(
        );
        this.stringtovaluemaps = new ArrayList<>();
    }

    public model_values_Metadata(
        ArrayList<StringToValueMap> stringtovaluemaps    ) {
        this.stringtovaluemaps = stringtovaluemaps;
    }


    public List<StringToValueMap> getStringtovaluemaps() {
        return stringtovaluemaps;
    }

    public void addStringtovaluemap(Stringtovaluemap stringtovaluemap) {
        this.stringtovaluemaps.add(stringtovaluemap);
    }

}