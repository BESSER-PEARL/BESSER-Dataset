





import java.util.List;
import java.util.ArrayList;

public class idl_Declarator  {

    private String id;





    private idl_Member idl_member;


    public idl_Declarator(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public idl_Member getIdl_member() {
        return idl_member;
    }

    public void setIdl_member(idl_Member idl_member) {
        this.idl_member = idl_member;
    }

}