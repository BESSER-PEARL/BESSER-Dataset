





import java.util.List;
import java.util.ArrayList;

public class idl_ParameterDecls  {






    private idl_FactoryDcl idl_factorydcl;




    private idl_FinderDcl idl_finderdcl;




    private List<idl_IDLComment> idl_idlcomments;




    private idl_OpDecl idl_opdecl;


    public idl_ParameterDecls(
    ) {
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_ParameterDecls(
        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.idl_idlcomments = idl_idlcomments;
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
    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }
    public idl_OpDecl getIdl_opdecl() {
        return idl_opdecl;
    }

    public void setIdl_opdecl(idl_OpDecl idl_opdecl) {
        this.idl_opdecl = idl_opdecl;
    }

}