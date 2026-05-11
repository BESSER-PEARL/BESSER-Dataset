





import java.util.List;
import java.util.ArrayList;

public class idl_Case  {






    private List<idl_IDLComment> idl_idlcomments;




    private idl_SwitchBody idl_switchbody;


    public idl_Case(
    ) {
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_Case(
        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.idl_idlcomments = idl_idlcomments;
    }


    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }
    public idl_SwitchBody getIdl_switchbody() {
        return idl_switchbody;
    }

    public void setIdl_switchbody(idl_SwitchBody idl_switchbody) {
        this.idl_switchbody = idl_switchbody;
    }

}