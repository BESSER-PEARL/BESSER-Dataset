





import java.util.List;
import java.util.ArrayList;

public class express_core_ScopedId  {

    private String localName;





    private Scope scope;


    public express_core_ScopedId(
        String localName    ) {
        this.localName = localName;
    }


    public String getLocalname() {
        return localName;
    }

    public void setLocalname(String localName) {
        this.localName = localName;
    }

    public Scope getScope() {
        return scope;
    }

    public void setScope(Scope scope) {
        this.scope = scope;
    }

}