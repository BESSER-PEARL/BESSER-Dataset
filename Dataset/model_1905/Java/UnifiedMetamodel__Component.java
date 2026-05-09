





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Component  {

    private String name;





    private List<UnifiedMetamodel__Layer> unifiedmetamodel__layers;


    public UnifiedMetamodel__Component(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__layers = new ArrayList<>();
    }

    public UnifiedMetamodel__Component(
        String name        ArrayList<UnifiedMetamodel__Layer> unifiedmetamodel__layers    ) {
        this.name = name;
        this.unifiedmetamodel__layers = unifiedmetamodel__layers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<UnifiedMetamodel__Layer> getUnifiedmetamodel__layers() {
        return unifiedmetamodel__layers;
    }

    public void addUnifiedmetamodel__layer(Unifiedmetamodel__layer unifiedmetamodel__layer) {
        this.unifiedmetamodel__layers.add(unifiedmetamodel__layer);
    }

}