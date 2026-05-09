





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__AbstractMethod  {

    private String name;





    private UnifiedMetamodel__EClass unifiedmetamodel__eclass;




    private List<UnifiedMetamodel__EClass> unifiedmetamodel__eclasss;




    private UnifiedMetamodel__EInterface unifiedmetamodel__einterface;




    private UnifiedMetamodel__AbstractClass unifiedmetamodel__abstractclass;


    public UnifiedMetamodel__AbstractMethod(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__eclasss = new ArrayList<>();
    }

    public UnifiedMetamodel__AbstractMethod(
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

    public UnifiedMetamodel__EClass getUnifiedmetamodel__eclass() {
        return unifiedmetamodel__eclass;
    }

    public void setUnifiedmetamodel__eclass(UnifiedMetamodel__EClass unifiedmetamodel__eclass) {
        this.unifiedmetamodel__eclass = unifiedmetamodel__eclass;
    }
    public List<UnifiedMetamodel__EClass> getUnifiedmetamodel__eclasss() {
        return unifiedmetamodel__eclasss;
    }

    public void addUnifiedmetamodel__eclass(Unifiedmetamodel__eclass unifiedmetamodel__eclass) {
        this.unifiedmetamodel__eclasss.add(unifiedmetamodel__eclass);
    }
    public UnifiedMetamodel__EInterface getUnifiedmetamodel__einterface() {
        return unifiedmetamodel__einterface;
    }

    public void setUnifiedmetamodel__einterface(UnifiedMetamodel__EInterface unifiedmetamodel__einterface) {
        this.unifiedmetamodel__einterface = unifiedmetamodel__einterface;
    }
    public UnifiedMetamodel__AbstractClass getUnifiedmetamodel__abstractclass() {
        return unifiedmetamodel__abstractclass;
    }

    public void setUnifiedmetamodel__abstractclass(UnifiedMetamodel__AbstractClass unifiedmetamodel__abstractclass) {
        this.unifiedmetamodel__abstractclass = unifiedmetamodel__abstractclass;
    }

}