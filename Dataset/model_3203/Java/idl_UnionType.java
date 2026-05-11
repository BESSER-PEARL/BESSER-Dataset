





import java.util.List;
import java.util.ArrayList;

public class idl_UnionType extends ConstrTypeSpec, TypeDecl {

    private String name;





    private List<idl_IDLComment> idl_idlcomments;


    public idl_UnionType(
        String name    ) {
        super(
        );
        this.name = name;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_UnionType(
        String name        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.name = name;
        this.idl_idlcomments = idl_idlcomments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}