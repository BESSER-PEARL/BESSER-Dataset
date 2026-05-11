





import java.util.List;
import java.util.ArrayList;

public class etrace_ETrace extends CompositeLink {

    private String name;





    private List<etrace_EObject> etrace_eobjects;




    private List<etrace_LinkType> etrace_linktypes;




    private List<etrace_EObject> etrace_eobjects;


    public etrace_ETrace(
        String name    ) {
        super(
        );
        this.name = name;
        this.etrace_eobjects = new ArrayList<>();
        this.etrace_linktypes = new ArrayList<>();
        this.etrace_eobjects = new ArrayList<>();
    }

    public etrace_ETrace(
        String name        ArrayList<etrace_EObject> etrace_eobjects,        ArrayList<etrace_LinkType> etrace_linktypes,        ArrayList<etrace_EObject> etrace_eobjects    ) {
        this.name = name;
        this.etrace_eobjects = etrace_eobjects;
        this.etrace_linktypes = etrace_linktypes;
        this.etrace_eobjects = etrace_eobjects;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<etrace_EObject> getEtrace_eobjects() {
        return etrace_eobjects;
    }

    public void addEtrace_eobject(Etrace_eobject etrace_eobject) {
        this.etrace_eobjects.add(etrace_eobject);
    }
    public List<etrace_LinkType> getEtrace_linktypes() {
        return etrace_linktypes;
    }

    public void addEtrace_linktype(Etrace_linktype etrace_linktype) {
        this.etrace_linktypes.add(etrace_linktype);
    }
    public List<etrace_EObject> getEtrace_eobjects() {
        return etrace_eobjects;
    }

    public void addEtrace_eobject(Etrace_eobject etrace_eobject) {
        this.etrace_eobjects.add(etrace_eobject);
    }

}