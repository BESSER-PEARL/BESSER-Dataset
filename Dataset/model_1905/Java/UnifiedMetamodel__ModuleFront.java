





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__ModuleFront  {

    private String name;





    private UnifiedMetamodel__ComponentFront unifiedmetamodel__componentfront;




    private UnifiedMetamodel__Directory unifiedmetamodel__directory;




    private UnifiedMetamodel__ServicesFront unifiedmetamodel__servicesfront;




    private UnifiedMetamodel__State unifiedmetamodel__state;


    public UnifiedMetamodel__ModuleFront(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UnifiedMetamodel__ComponentFront getUnifiedmetamodel__componentfront() {
        return unifiedmetamodel__componentfront;
    }

    public void setUnifiedmetamodel__componentfront(UnifiedMetamodel__ComponentFront unifiedmetamodel__componentfront) {
        this.unifiedmetamodel__componentfront = unifiedmetamodel__componentfront;
    }
    public UnifiedMetamodel__Directory getUnifiedmetamodel__directory() {
        return unifiedmetamodel__directory;
    }

    public void setUnifiedmetamodel__directory(UnifiedMetamodel__Directory unifiedmetamodel__directory) {
        this.unifiedmetamodel__directory = unifiedmetamodel__directory;
    }
    public UnifiedMetamodel__ServicesFront getUnifiedmetamodel__servicesfront() {
        return unifiedmetamodel__servicesfront;
    }

    public void setUnifiedmetamodel__servicesfront(UnifiedMetamodel__ServicesFront unifiedmetamodel__servicesfront) {
        this.unifiedmetamodel__servicesfront = unifiedmetamodel__servicesfront;
    }
    public UnifiedMetamodel__State getUnifiedmetamodel__state() {
        return unifiedmetamodel__state;
    }

    public void setUnifiedmetamodel__state(UnifiedMetamodel__State unifiedmetamodel__state) {
        this.unifiedmetamodel__state = unifiedmetamodel__state;
    }

}