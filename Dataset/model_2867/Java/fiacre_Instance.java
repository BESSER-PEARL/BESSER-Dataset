





import java.util.List;
import java.util.ArrayList;

public class fiacre_Instance extends Composition {

    private String name;





    private List<fiacre_PortDecl> fiacre_portdecls;




    private List<fiacre_Arg> fiacre_args;




    private fiacre_NodeDecl fiacre_nodedecl;


    public fiacre_Instance(
        String name    ) {
        super(
        );
        this.name = name;
        this.fiacre_portdecls = new ArrayList<>();
        this.fiacre_args = new ArrayList<>();
    }

    public fiacre_Instance(
        String name        ArrayList<fiacre_PortDecl> fiacre_portdecls,        ArrayList<fiacre_Arg> fiacre_args    ) {
        this.name = name;
        this.fiacre_portdecls = fiacre_portdecls;
        this.fiacre_args = fiacre_args;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<fiacre_PortDecl> getFiacre_portdecls() {
        return fiacre_portdecls;
    }

    public void addFiacre_portdecl(Fiacre_portdecl fiacre_portdecl) {
        this.fiacre_portdecls.add(fiacre_portdecl);
    }
    public List<fiacre_Arg> getFiacre_args() {
        return fiacre_args;
    }

    public void addFiacre_arg(Fiacre_arg fiacre_arg) {
        this.fiacre_args.add(fiacre_arg);
    }
    public fiacre_NodeDecl getFiacre_nodedecl() {
        return fiacre_nodedecl;
    }

    public void setFiacre_nodedecl(fiacre_NodeDecl fiacre_nodedecl) {
        this.fiacre_nodedecl = fiacre_nodedecl;
    }

}