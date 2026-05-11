





import java.util.List;
import java.util.ArrayList;

public class idl_Member  {






    private List<idl_IDLComment> idl_idlcomments;




    private idl_ExceptDecl idl_exceptdecl;


    public idl_Member(
    ) {
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_Member(
        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.idl_idlcomments = idl_idlcomments;
    }


    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }
    public idl_ExceptDecl getIdl_exceptdecl() {
        return idl_exceptdecl;
    }

    public void setIdl_exceptdecl(idl_ExceptDecl idl_exceptdecl) {
        this.idl_exceptdecl = idl_exceptdecl;
    }

}