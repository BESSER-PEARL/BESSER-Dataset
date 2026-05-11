





import java.util.List;
import java.util.ArrayList;

public class idl_Member  {






    private idl_TypeSpec idl_typespec;




    private idl_ExceptDecl idl_exceptdecl;




    private idl_StructType idl_structtype;




    private List<idl_IDLComment> idl_idlcomments;


    public idl_Member(
    ) {
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_Member(
        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.idl_idlcomments = idl_idlcomments;
    }


    public idl_TypeSpec getIdl_typespec() {
        return idl_typespec;
    }

    public void setIdl_typespec(idl_TypeSpec idl_typespec) {
        this.idl_typespec = idl_typespec;
    }
    public idl_ExceptDecl getIdl_exceptdecl() {
        return idl_exceptdecl;
    }

    public void setIdl_exceptdecl(idl_ExceptDecl idl_exceptdecl) {
        this.idl_exceptdecl = idl_exceptdecl;
    }
    public idl_StructType getIdl_structtype() {
        return idl_structtype;
    }

    public void setIdl_structtype(idl_StructType idl_structtype) {
        this.idl_structtype = idl_structtype;
    }
    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}