





import java.util.List;
import java.util.ArrayList;

public class UnifiedMetamodel__Property  {

    private String type;
    private String name;





    private UnifiedMetamodel__Entity unifiedmetamodel__entity;


    public UnifiedMetamodel__Property(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public UnifiedMetamodel__Entity getUnifiedmetamodel__entity() {
        return unifiedmetamodel__entity;
    }

    public void setUnifiedmetamodel__entity(UnifiedMetamodel__Entity unifiedmetamodel__entity) {
        this.unifiedmetamodel__entity = unifiedmetamodel__entity;
    }

}