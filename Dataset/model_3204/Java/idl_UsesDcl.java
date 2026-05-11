





import java.util.List;
import java.util.ArrayList;

public class idl_UsesDcl extends ComponentExport, PortExport, ConnectorExport {

    private String name;
    private boolean isMultiple;





    private List<idl_IDLComment> idl_idlcomments;




    private idl_ScopedName idl_scopedname;


    public idl_UsesDcl(
        String name,        boolean isMultiple    ) {
        super(
        );
        this.name = name;
        this.isMultiple = isMultiple;
        this.idl_idlcomments = new ArrayList<>();
    }

    public idl_UsesDcl(
        String name,        boolean isMultiple        ArrayList<idl_IDLComment> idl_idlcomments    ) {
        this.name = name;
        this.isMultiple = isMultiple;
        this.idl_idlcomments = idl_idlcomments;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getIsmultiple() {
        return isMultiple;
    }

    public void setIsmultiple(boolean isMultiple) {
        this.isMultiple = isMultiple;
    }

    public List<idl_IDLComment> getIdl_idlcomments() {
        return idl_idlcomments;
    }

    public void addIdl_idlcomment(Idl_idlcomment idl_idlcomment) {
        this.idl_idlcomments.add(idl_idlcomment);
    }
    public idl_ScopedName getIdl_scopedname() {
        return idl_scopedname;
    }

    public void setIdl_scopedname(idl_ScopedName idl_scopedname) {
        this.idl_scopedname = idl_scopedname;
    }

}