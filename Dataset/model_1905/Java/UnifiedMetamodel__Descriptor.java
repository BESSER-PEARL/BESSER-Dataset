





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Descriptor  {

    private String name;
    private String path;





    private UnifiedMetamodel__Annotation unifiedmetamodel__annotation;




    private UnifiedMetamodel__Subproject unifiedmetamodel__subproject;


    public UnifiedMetamodel__Descriptor(
        String name,        String path    ) {
        this.name = name;
        this.path = path;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }

    public UnifiedMetamodel__Annotation getUnifiedmetamodel__annotation() {
        return unifiedmetamodel__annotation;
    }

    public void setUnifiedmetamodel__annotation(UnifiedMetamodel__Annotation unifiedmetamodel__annotation) {
        this.unifiedmetamodel__annotation = unifiedmetamodel__annotation;
    }
    public UnifiedMetamodel__Subproject getUnifiedmetamodel__subproject() {
        return unifiedmetamodel__subproject;
    }

    public void setUnifiedmetamodel__subproject(UnifiedMetamodel__Subproject unifiedmetamodel__subproject) {
        this.unifiedmetamodel__subproject = unifiedmetamodel__subproject;
    }

}