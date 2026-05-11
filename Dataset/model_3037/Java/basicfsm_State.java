





import java.util.List;
import java.util.ArrayList;

public class basicfsm_State  {

    private String name;





    private List<basicfsm_Trans> basicfsm_transs;




    private List<basicfsm_VarDecl> basicfsm_vardecls;




    private List<basicfsm_Trans> basicfsm_transs;




    private basicfsm_Trans basicfsm_trans;




    private basicfsm_Machine basicfsm_machine;




    private basicfsm_Trans basicfsm_trans;


    public basicfsm_State(
        String name    ) {
        this.name = name;
        this.basicfsm_transs = new ArrayList<>();
        this.basicfsm_vardecls = new ArrayList<>();
        this.basicfsm_transs = new ArrayList<>();
    }

    public basicfsm_State(
        String name        ArrayList<basicfsm_Trans> basicfsm_transs,        ArrayList<basicfsm_VarDecl> basicfsm_vardecls,        ArrayList<basicfsm_Trans> basicfsm_transs    ) {
        this.name = name;
        this.basicfsm_transs = basicfsm_transs;
        this.basicfsm_vardecls = basicfsm_vardecls;
        this.basicfsm_transs = basicfsm_transs;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<basicfsm_Trans> getBasicfsm_transs() {
        return basicfsm_transs;
    }

    public void addBasicfsm_trans(Basicfsm_trans basicfsm_trans) {
        this.basicfsm_transs.add(basicfsm_trans);
    }
    public List<basicfsm_VarDecl> getBasicfsm_vardecls() {
        return basicfsm_vardecls;
    }

    public void addBasicfsm_vardecl(Basicfsm_vardecl basicfsm_vardecl) {
        this.basicfsm_vardecls.add(basicfsm_vardecl);
    }
    public List<basicfsm_Trans> getBasicfsm_transs() {
        return basicfsm_transs;
    }

    public void addBasicfsm_trans(Basicfsm_trans basicfsm_trans) {
        this.basicfsm_transs.add(basicfsm_trans);
    }
    public basicfsm_Trans getBasicfsm_trans() {
        return basicfsm_trans;
    }

    public void setBasicfsm_trans(basicfsm_Trans basicfsm_trans) {
        this.basicfsm_trans = basicfsm_trans;
    }
    public basicfsm_Machine getBasicfsm_machine() {
        return basicfsm_machine;
    }

    public void setBasicfsm_machine(basicfsm_Machine basicfsm_machine) {
        this.basicfsm_machine = basicfsm_machine;
    }
    public basicfsm_Trans getBasicfsm_trans() {
        return basicfsm_trans;
    }

    public void setBasicfsm_trans(basicfsm_Trans basicfsm_trans) {
        this.basicfsm_trans = basicfsm_trans;
    }

}