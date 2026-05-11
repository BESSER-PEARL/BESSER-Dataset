





import java.util.List;
import java.util.ArrayList;

public class idl_ConstDecl extends TemplateDefinition, Export, Definition, FixedDefinition {

    private String name;





    private idl_ConstExp idl_constexp;




    private List<idl_IDLComment> idl_idlcomments;


    public idl_ConstDecl(
        String name    ) {
        super(
        );
        this.name = name;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_ConstDecl(
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

    public idl_ConstExp getIdl_constexp() {
        return idl_constexp;
    }

    public void setIdl_constexp(idl_ConstExp idl_constexp) {
        this.idl_constexp = idl_constexp;
    }
    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}