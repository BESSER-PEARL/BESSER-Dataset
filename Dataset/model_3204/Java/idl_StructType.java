





import java.util.List;
import java.util.ArrayList;

public class idl_StructType extends TypeDecl, Definition, ConstrTypeSpec {

    private String name;





    private List<idl_IDLComment> idl_idlcomments;




    private List<idl_Member> idl_members;


    public idl_StructType(
        String name    ) {
        super(
        );
        this.name = name;
        this.idl_idlcomments = new ArrayList<>();
        this.idl_members = new ArrayList<>();
    }

    public idl_StructType(
        String name        ArrayList<idl_IDLComment> idl_idlcomments,        ArrayList<idl_Member> idl_members    ) {
        this.name = name;
        this.idl_idlcomments = idl_idlcomments;
        this.idl_members = idl_members;
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
    public List<idl_Member> getIdl_members() {
        return idl_members;
    }

    public void addIdl_member(Idl_member idl_member) {
        this.idl_members.add(idl_member);
    }

}