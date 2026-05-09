





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Directory  {

    private boolean isRoot;
    private String name;
    private String purpose;





    private List<UnifiedMetamodel__Directory> unifiedmetamodel__directorys;


    public UnifiedMetamodel__Directory(
        boolean isRoot,        String name,        String purpose    ) {
        this.isRoot = isRoot;
        this.name = name;
        this.purpose = purpose;
        this.unifiedmetamodel__directorys = new ArrayList<>();
    }

    public UnifiedMetamodel__Directory(
        boolean isRoot,        String name,        String purpose        ArrayList<UnifiedMetamodel__Directory> unifiedmetamodel__directorys    ) {
        this.isRoot = isRoot;
        this.name = name;
        this.purpose = purpose;
        this.unifiedmetamodel__directorys = unifiedmetamodel__directorys;
    }

    public boolean getIsroot() {
        return isRoot;
    }

    public void setIsroot(boolean isRoot) {
        this.isRoot = isRoot;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPurpose() {
        return purpose;
    }

    public void setPurpose(String purpose) {
        this.purpose = purpose;
    }

    public List<UnifiedMetamodel__Directory> getUnifiedmetamodel__directorys() {
        return unifiedmetamodel__directorys;
    }

    public void addUnifiedmetamodel__directory(Unifiedmetamodel__directory unifiedmetamodel__directory) {
        this.unifiedmetamodel__directorys.add(unifiedmetamodel__directory);
    }

}