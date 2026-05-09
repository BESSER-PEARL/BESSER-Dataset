





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Functionality  {

    private String name;





    private List<UnifiedMetamodel__ServicesFront> unifiedmetamodel__servicesfronts;




    private UnifiedMetamodel__Directory unifiedmetamodel__directory;


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
    public UnifiedMetamodel__Directory getUnifiedmetamodel__directory() {
        return unifiedmetamodel__directory;
    }

    public void setUnifiedmetamodel__directory(UnifiedMetamodel__Directory unifiedmetamodel__directory) {
        this.unifiedmetamodel__directory = unifiedmetamodel__directory;
    }

}