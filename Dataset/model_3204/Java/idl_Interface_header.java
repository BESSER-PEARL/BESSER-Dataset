





import java.util.List;
import java.util.ArrayList;

public class idl_Interface_header  {

    private boolean isLocal;
    private String name;
    private boolean isAbstract;





    private idl_Interface_decl idl_interface_decl;




    private List<idl_IDLComment> idl_idlcomments;


    public idl_Interface_header(
        boolean isLocal,        String name,        boolean isAbstract    ) {
        this.isLocal = isLocal;
        this.name = name;
        this.isAbstract = isAbstract;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_Interface_header(
        boolean isLocal,        String name,        boolean isAbstract        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.isLocal = isLocal;
        this.name = name;
        this.isAbstract = isAbstract;
        this.idl_idlcomments = idl_idlcomments;
    }

    public boolean getIslocal() {
        return isLocal;
    }

    public void setIslocal(boolean isLocal) {
        this.isLocal = isLocal;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsabstract() {
        return isAbstract;
    }

    public void setIsabstract(boolean isAbstract) {
        this.isAbstract = isAbstract;
    }

    public idl_Interface_decl getIdl_interface_decl() {
        return idl_interface_decl;
    }

    public void setIdl_interface_decl(idl_Interface_decl idl_interface_decl) {
        this.idl_interface_decl = idl_interface_decl;
    }
    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}