





import java.util.List;
import java.util.ArrayList;

public class idl_ParameterDecls  {






    private idl_OpDecl idl_opdecl;




    private List<idl_IDLComment> idl_idlcomments;


    public idl_ParameterDecls(
    ) {
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_ParameterDecls(
        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.idl_idlcomments = idl_idlcomments;
    }


    public idl_OpDecl getIdl_opdecl() {
        return idl_opdecl;
    }

    public void setIdl_opdecl(idl_OpDecl idl_opdecl) {
        this.idl_opdecl = idl_opdecl;
    }
    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}