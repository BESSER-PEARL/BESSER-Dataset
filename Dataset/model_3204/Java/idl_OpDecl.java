





import java.util.List;
import java.util.ArrayList;

public class idl_OpDecl extends Export {

    private String name;
    private boolean isOneway;





    private List<idl_IDLComment> idl_idlcomments;




    private idl_ExceptionList idl_exceptionlist;


    public idl_OpDecl(
        String name,        boolean isOneway    ) {
        super(
        );
        this.name = name;
        this.isOneway = isOneway;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_OpDecl(
        String name,        boolean isOneway        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.name = name;
        this.isOneway = isOneway;
        this.idl_idlcomments = idl_idlcomments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsoneway() {
        return isOneway;
    }

    public void setIsoneway(boolean isOneway) {
        this.isOneway = isOneway;
    }

    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }
    public idl_ExceptionList getIdl_exceptionlist() {
        return idl_exceptionlist;
    }

    public void setIdl_exceptionlist(idl_ExceptionList idl_exceptionlist) {
        this.idl_exceptionlist = idl_exceptionlist;
    }

}