





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__RouterComponent extends UIFront {






    private List<UnifiedMetamodel__UIFront> unifiedmetamodel__uifronts;


    public UnifiedMetamodel__RouterComponent(
    ) {
        super(
        );
        this.unifiedmetamodel__uifronts = new ArrayList<>();
    }

    public UnifiedMetamodel__RouterComponent(
        ArrayList<UnifiedMetamodel__UIFront> unifiedmetamodel__uifronts    ) {
        this.unifiedmetamodel__uifronts = unifiedmetamodel__uifronts;
    }


    public List<UnifiedMetamodel__UIFront> getUnifiedmetamodel__uifronts() {
        return unifiedmetamodel__uifronts;
    }

    public void addUnifiedmetamodel__uifront(Unifiedmetamodel__uifront unifiedmetamodel__uifront) {
        this.unifiedmetamodel__uifronts.add(unifiedmetamodel__uifront);
    }

}