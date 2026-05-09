





import java.util.List;
import java.util.ArrayList;

public class express_core_NamedElement  {






    private ScopedId scopedid;




    private List<Remark> remarks;




    private Scope scope;


    public express_core_NamedElement(
    ) {
        this.remarks = new ArrayList<>();
    }

    public express_core_NamedElement(
        ArrayList<Remark> remarks    ) {
        this.remarks = remarks;
    }


    public ScopedId getScopedid() {
        return scopedid;
    }

    public void setScopedid(ScopedId scopedid) {
        this.scopedid = scopedid;
    }
    public List<Remark> getRemarks() {
        return remarks;
    }

    public void addRemark(Remark remark) {
        this.remarks.add(remark);
    }
    public Scope getScope() {
        return scope;
    }

    public void setScope(Scope scope) {
        this.scope = scope;
    }

}