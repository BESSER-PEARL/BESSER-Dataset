





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Action  {

    private String name;





    private List<UnifiedMetamodel__ActionDispatcher> unifiedmetamodel__actiondispatchers;




    private UnifiedMetamodel__State unifiedmetamodel__state;




    private List<UnifiedMetamodel__ActionCreator> unifiedmetamodel__actioncreators;




    private UnifiedMetamodel__Directory unifiedmetamodel__directory;


    public UnifiedMetamodel__Action(
        String name    ) {
        this.name = name;
        this.unifiedmetamodel__actiondispatchers = new ArrayList<>();
        this.unifiedmetamodel__actioncreators = new ArrayList<>();
    }

    public UnifiedMetamodel__Action(
        String name        ArrayList<UnifiedMetamodel__ActionDispatcher> unifiedmetamodel__actiondispatchers,        ArrayList<UnifiedMetamodel__ActionCreator> unifiedmetamodel__actioncreators    ) {
        this.name = name;
        this.unifiedmetamodel__actiondispatchers = unifiedmetamodel__actiondispatchers;
        this.unifiedmetamodel__actioncreators = unifiedmetamodel__actioncreators;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<UnifiedMetamodel__ActionDispatcher> getUnifiedmetamodel__actiondispatchers() {
        return unifiedmetamodel__actiondispatchers;
    }

    public void addUnifiedmetamodel__actiondispatcher(Unifiedmetamodel__actiondispatcher unifiedmetamodel__actiondispatcher) {
        this.unifiedmetamodel__actiondispatchers.add(unifiedmetamodel__actiondispatcher);
    }
    public UnifiedMetamodel__State getUnifiedmetamodel__state() {
        return unifiedmetamodel__state;
    }

    public void setUnifiedmetamodel__state(UnifiedMetamodel__State unifiedmetamodel__state) {
        this.unifiedmetamodel__state = unifiedmetamodel__state;
    }
    public List<UnifiedMetamodel__ActionCreator> getUnifiedmetamodel__actioncreators() {
        return unifiedmetamodel__actioncreators;
    }

    public void addUnifiedmetamodel__actioncreator(Unifiedmetamodel__actioncreator unifiedmetamodel__actioncreator) {
        this.unifiedmetamodel__actioncreators.add(unifiedmetamodel__actioncreator);
    }
    public UnifiedMetamodel__Directory getUnifiedmetamodel__directory() {
        return unifiedmetamodel__directory;
    }

    public void setUnifiedmetamodel__directory(UnifiedMetamodel__Directory unifiedmetamodel__directory) {
        this.unifiedmetamodel__directory = unifiedmetamodel__directory;
    }

}