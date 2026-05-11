





import java.util.List;
import java.util.ArrayList;

public class idl_FinderDcl extends HomeExport {

    private String name;





    private idl_ParameterDecls idl_parameterdecls;




    private idl_ExceptionList idl_exceptionlist;




    private List<idl_IDLComment> idl_idlcomments;


    public idl_FinderDcl(
        String name    ) {
        super(
        );
        this.name = name;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_FinderDcl(
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

    public idl_ParameterDecls getIdl_parameterdecls() {
        return idl_parameterdecls;
    }

    public void setIdl_parameterdecls(idl_ParameterDecls idl_parameterdecls) {
        this.idl_parameterdecls = idl_parameterdecls;
    }
    public idl_ExceptionList getIdl_exceptionlist() {
        return idl_exceptionlist;
    }

    public void setIdl_exceptionlist(idl_ExceptionList idl_exceptionlist) {
        this.idl_exceptionlist = idl_exceptionlist;
    }
    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}