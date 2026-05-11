





import java.util.List;
import java.util.ArrayList;

public class idl_TypeDeclarator extends TypeDecl {






    private List<idl_IDLComment> idl_idlcomments;


    public idl_TypeDeclarator(
    ) {
        super(
        );
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_TypeDeclarator(
        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.idl_idlcomments = idl_idlcomments;
    }


    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}