





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Submodule  {

    private String name;





    private UnifiedMetamodel__Module unifiedmetamodel__module;




    private List<UnifiedMetamodel__Entity> unifiedmetamodel__entitys;




    private List<UnifiedMetamodel__Operations> unifiedmetamodel__operationss;


    public UnifiedMetamodel__Submodule(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__entitys = new ArrayList<>();
        this.unifiedmetamodel__operationss = new ArrayList<>();
    }

    public UnifiedMetamodel__Submodule(
        String name        ArrayList<UnifiedMetamodel__Entity> unifiedmetamodel__entitys,        ArrayList<UnifiedMetamodel__Operations> unifiedmetamodel__operationss    ) {
        this.name = name;
        this.unifiedmetamodel__entitys = unifiedmetamodel__entitys;
        this.unifiedmetamodel__operationss = unifiedmetamodel__operationss;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UnifiedMetamodel__Module getUnifiedmetamodel__module() {
        return unifiedmetamodel__module;
    }

    public void setUnifiedmetamodel__module(UnifiedMetamodel__Module unifiedmetamodel__module) {
        this.unifiedmetamodel__module = unifiedmetamodel__module;
    }
    public List<UnifiedMetamodel__Entity> getUnifiedmetamodel__entitys() {
        return unifiedmetamodel__entitys;
    }

    public void addUnifiedmetamodel__entity(Unifiedmetamodel__entity unifiedmetamodel__entity) {
        this.unifiedmetamodel__entitys.add(unifiedmetamodel__entity);
    }
    public List<UnifiedMetamodel__Operations> getUnifiedmetamodel__operationss() {
        return unifiedmetamodel__operationss;
    }

    public void addUnifiedmetamodel__operations(Unifiedmetamodel__operations unifiedmetamodel__operations) {
        this.unifiedmetamodel__operationss.add(unifiedmetamodel__operations);
    }

}