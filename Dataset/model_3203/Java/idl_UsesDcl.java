





import java.util.List;
import java.util.ArrayList;

public class idl_UsesDcl extends PortExport, ComponentExport, ConnectorExport {

    private boolean isMultiple;
    private String name;





    private List<idl_IDLComment> idl_idlcomments;


    public idl_UsesDcl(
        boolean isMultiple,        String name    ) {
        super(
        );
        this.isMultiple = isMultiple;
        this.name = name;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_UsesDcl(
        boolean isMultiple,        String name        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.isMultiple = isMultiple;
        this.name = name;
        this.idl_idlcomments = idl_idlcomments;
    }

    public boolean getIsmultiple() {
        return isMultiple;
    }

    public void setIsmultiple(boolean isMultiple) {
        this.isMultiple = isMultiple;
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

}