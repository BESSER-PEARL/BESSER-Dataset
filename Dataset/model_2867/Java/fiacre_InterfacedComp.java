





import java.util.List;
import java.util.ArrayList;

public class fiacre_InterfacedComp  {






    private fiacre_Composition fiacre_composition;




    private fiacre_Par fiacre_par;




    private List<fiacre_PortDecl> fiacre_portdecls;


    public fiacre_InterfacedComp(
    ) {
        this.fiacre_portdecls = new ArrayList<>();
    }

    public fiacre_InterfacedComp(
        ArrayList<fiacre_PortDecl> fiacre_portdecls    ) {
        this.fiacre_portdecls = fiacre_portdecls;
    }


    public fiacre_Composition getFiacre_composition() {
        return fiacre_composition;
    }

    public void setFiacre_composition(fiacre_Composition fiacre_composition) {
        this.fiacre_composition = fiacre_composition;
    }
    public fiacre_Par getFiacre_par() {
        return fiacre_par;
    }

    public void setFiacre_par(fiacre_Par fiacre_par) {
        this.fiacre_par = fiacre_par;
    }
    public List<fiacre_PortDecl> getFiacre_portdecls() {
        return fiacre_portdecls;
    }

    public void addFiacre_portdecl(Fiacre_portdecl fiacre_portdecl) {
        this.fiacre_portdecls.add(fiacre_portdecl);
    }

}