





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__MethodBack  {

    private String name;





    private List<UnifiedMetamodel__EClass> unifiedmetamodel__eclasss;




    private UnifiedMetamodel__EClass unifiedmetamodel__eclass;




    private UnifiedMetamodel__Annotation unifiedmetamodel__annotation;




    private UnifiedMetamodel__EClass unifiedmetamodel__eclass;


    public UnifiedMetamodel__MethodBack(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__eclasss = new ArrayList<>();
    }

    public UnifiedMetamodel__MethodBack(
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
    public UnifiedMetamodel__EClass getUnifiedmetamodel__eclass() {
        return unifiedmetamodel__eclass;
    }

    public void setUnifiedmetamodel__eclass(UnifiedMetamodel__EClass unifiedmetamodel__eclass) {
        this.unifiedmetamodel__eclass = unifiedmetamodel__eclass;
    }
    public UnifiedMetamodel__Annotation getUnifiedmetamodel__annotation() {
        return unifiedmetamodel__annotation;
    }

    public void setUnifiedmetamodel__annotation(UnifiedMetamodel__Annotation unifiedmetamodel__annotation) {
        this.unifiedmetamodel__annotation = unifiedmetamodel__annotation;
    }
    public UnifiedMetamodel__EClass getUnifiedmetamodel__eclass() {
        return unifiedmetamodel__eclass;
    }

    public void setUnifiedmetamodel__eclass(UnifiedMetamodel__EClass unifiedmetamodel__eclass) {
        this.unifiedmetamodel__eclass = unifiedmetamodel__eclass;
    }

}