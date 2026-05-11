





import java.util.List;
import java.util.ArrayList;

public class idl_PortDecl extends ComponentExport, ConnectorExport {

    private String name;
    private boolean isMirror;





    private List<idl_IDLComment> idl_idlcomments;


    public idl_PortDecl(
        String name,        boolean isMirror    ) {
        super(
        );
        this.name = name;
        this.isMirror = isMirror;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_PortDecl(
        String name,        boolean isMirror        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.name = name;
        this.isMirror = isMirror;
        this.idl_idlcomments = idl_idlcomments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsmirror() {
        return isMirror;
    }

    public void setIsmirror(boolean isMirror) {
        this.isMirror = isMirror;
    }

    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}