





import java.util.List;
import java.util.ArrayList;

public class idl_EnumType extends ConstrTypeSpec, SwitchTypeSpec, TypeDecl {

    private String name;
    private String literal;





    private List<idl_IDLComment> idl_idlcomments;


    public idl_EnumType(
        String name,        String literal    ) {
        super(
        );
        this.name = name;
        this.literal = literal;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_EnumType(
        String name,        String literal        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.name = name;
        this.literal = literal;
        this.idl_idlcomments = idl_idlcomments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLiteral() {
        return literal;
    }

    public void setLiteral(String literal) {
        this.literal = literal;
    }

    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}