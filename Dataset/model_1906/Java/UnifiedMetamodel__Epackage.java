





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Epackage  {

    private String name;





    private List<UnifiedMetamodel__EClass> unifiedmetamodel__eclasss;


    public UnifiedMetamodel__Epackage(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__eclasss = new ArrayList<>();
    }

    public UnifiedMetamodel__Epackage(
        String name        ArrayList<UnifiedMetamodel__EClass> unifiedmetamodel__eclasss    ) {
        this.name = name;
        this.unifiedmetamodel__eclasss = unifiedmetamodel__eclasss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<UnifiedMetamodel__EClass> getUnifiedmetamodel__eclasss() {
        return unifiedmetamodel__eclasss;
    }

    public void addUnifiedmetamodel__eclass(Unifiedmetamodel__eclass unifiedmetamodel__eclass) {
        this.unifiedmetamodel__eclasss.add(unifiedmetamodel__eclass);
    }

}