





import java.util.List;
import java.util.ArrayList;

public class idl_TypeDeclarator extends TypeDecl {






    private idl_TypeSpec idl_typespec;




    private List<idl_Declarator> idl_declarators;




    private List<idl_IDLComment> idl_idlcomments;


    public idl_TypeDeclarator(
    ) {
        super(
        );
        this.idl_declarators = new ArrayList<>();
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_TypeDeclarator(
        ArrayList<idl_Declarator> idl_declarators,        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.idl_declarators = idl_declarators;
        this.idl_idlcomments = idl_idlcomments;
    }


    public idl_TypeSpec getIdl_typespec() {
        return idl_typespec;
    }

    public void setIdl_typespec(idl_TypeSpec idl_typespec) {
        this.idl_typespec = idl_typespec;
    }
    public List<idl_Declarator> getIdl_declarators() {
        return idl_declarators;
    }

    public void addIdl_declarator(Idl_declarator idl_declarator) {
        this.idl_declarators.add(idl_declarator);
    }
    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}