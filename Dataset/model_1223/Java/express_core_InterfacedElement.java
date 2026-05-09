





import java.util.List;
import java.util.ArrayList;

public class express_core_InterfacedElement  {

    private String isUSE;





    private ScopedId scopedid;


    public express_core_InterfacedElement(
        String isUSE    ) {
        this.isUSE = isUSE;
    }


    public String getIsuse() {
        return isUSE;
    }

    public void setIsuse(String isUSE) {
        this.isUSE = isUSE;
    }

    public ScopedId getScopedid() {
        return scopedid;
    }

    public void setScopedid(ScopedId scopedid) {
        this.scopedid = scopedid;
    }

}