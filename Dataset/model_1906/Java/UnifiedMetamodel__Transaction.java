





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Transaction  {






    private List<UnifiedMetamodel__GeneralEntity> unifiedmetamodel__generalentitys;




    private UnifiedMetamodel__SpecialEntity unifiedmetamodel__specialentity;


    public UnifiedMetamodel__Transaction(
    ) {
        this.unifiedmetamodel__generalentitys = new ArrayList<>();
    }

    public UnifiedMetamodel__Transaction(
        ArrayList<UnifiedMetamodel__GeneralEntity> unifiedmetamodel__generalentitys    ) {
        this.unifiedmetamodel__generalentitys = unifiedmetamodel__generalentitys;
    }


    public List<UnifiedMetamodel__GeneralEntity> getUnifiedmetamodel__generalentitys() {
        return unifiedmetamodel__generalentitys;
    }

    public void addUnifiedmetamodel__generalentity(Unifiedmetamodel__generalentity unifiedmetamodel__generalentity) {
        this.unifiedmetamodel__generalentitys.add(unifiedmetamodel__generalentity);
    }
    public UnifiedMetamodel__SpecialEntity getUnifiedmetamodel__specialentity() {
        return unifiedmetamodel__specialentity;
    }

    public void setUnifiedmetamodel__specialentity(UnifiedMetamodel__SpecialEntity unifiedmetamodel__specialentity) {
        this.unifiedmetamodel__specialentity = unifiedmetamodel__specialentity;
    }

}