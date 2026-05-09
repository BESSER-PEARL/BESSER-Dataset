





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Functionality  {

    private String name;





    private List<UnifiedMetamodel__ServicesFront> unifiedmetamodel__servicesfronts;


    public UnifiedMetamodel__Functionality(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__servicesfronts = new ArrayList<>();
    }

    public UnifiedMetamodel__Functionality(
        String name        ArrayList<UnifiedMetamodel__ServicesFront> unifiedmetamodel__servicesfronts    ) {
        this.name = name;
        this.unifiedmetamodel__servicesfronts = unifiedmetamodel__servicesfronts;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<UnifiedMetamodel__ServicesFront> getUnifiedmetamodel__servicesfronts() {
        return unifiedmetamodel__servicesfronts;
    }

    public void addUnifiedmetamodel__servicesfront(Unifiedmetamodel__servicesfront unifiedmetamodel__servicesfront) {
        this.unifiedmetamodel__servicesfronts.add(unifiedmetamodel__servicesfront);
    }

}