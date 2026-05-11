





import java.util.List;
import java.util.ArrayList;

public class idl_ExceptionList  {






    private List<idl_ScopedName> idl_scopednames;




    private idl_FactoryDcl idl_factorydcl;




    private idl_FinderDcl idl_finderdcl;




    private idl_AttrRaisesExpr idl_attrraisesexpr;


    public idl_ExceptionList(
    ) {
        this.idl_scopednames = new ArrayList<>();
    }

    public idl_ExceptionList(
        ArrayList<idl_ScopedName> idl_scopednames    ) {
        this.idl_scopednames = idl_scopednames;
    }


    public List<idl_ScopedName> getIdl_scopednames() {
        return idl_scopednames;
    }

    public void addIdl_scopedname(Idl_scopedname idl_scopedname) {
        this.idl_scopednames.add(idl_scopedname);
    }
    public idl_FactoryDcl getIdl_factorydcl() {
        return idl_factorydcl;
    }

    public void setIdl_factorydcl(idl_FactoryDcl idl_factorydcl) {
        this.idl_factorydcl = idl_factorydcl;
    }
    public idl_FinderDcl getIdl_finderdcl() {
        return idl_finderdcl;
    }

    public void setIdl_finderdcl(idl_FinderDcl idl_finderdcl) {
        this.idl_finderdcl = idl_finderdcl;
    }
    public idl_AttrRaisesExpr getIdl_attrraisesexpr() {
        return idl_attrraisesexpr;
    }

    public void setIdl_attrraisesexpr(idl_AttrRaisesExpr idl_attrraisesexpr) {
        this.idl_attrraisesexpr = idl_attrraisesexpr;
    }

}