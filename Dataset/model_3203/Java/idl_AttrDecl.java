





import java.util.List;
import java.util.ArrayList;

public class idl_AttrDecl extends PortExport, ComponentExport, Export, ConnectorExport {

    private String names;





    private List<idl_IDLComment> idl_idlcomments;


    public idl_AttrDecl(
        String names    ) {
        super(
        );
        this.names = names;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_AttrDecl(
        String names        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.names = names;
        this.idl_idlcomments = idl_idlcomments;
    }

    public String getNames() {
        return names;
    }

    public void setNames(String names) {
        this.names = names;
    }

    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }

}