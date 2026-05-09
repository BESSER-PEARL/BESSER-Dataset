





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Container extends ComponentFront {






    private List<UnifiedMetamodel__ActionDispatcher> unifiedmetamodel__actiondispatchers;


    public UnifiedMetamodel__Container(
    ) {
        super(
        );
        this.unifiedmetamodel__actiondispatchers = new ArrayList<>();
    }

    public UnifiedMetamodel__Container(
        ArrayList<UnifiedMetamodel__ActionDispatcher> unifiedmetamodel__actiondispatchers    ) {
        this.unifiedmetamodel__actiondispatchers = unifiedmetamodel__actiondispatchers;
    }


    public List<UnifiedMetamodel__ActionDispatcher> getUnifiedmetamodel__actiondispatchers() {
        return unifiedmetamodel__actiondispatchers;
    }

    public void addUnifiedmetamodel__actiondispatcher(Unifiedmetamodel__actiondispatcher unifiedmetamodel__actiondispatcher) {
        this.unifiedmetamodel__actiondispatchers.add(unifiedmetamodel__actiondispatcher);
    }

}