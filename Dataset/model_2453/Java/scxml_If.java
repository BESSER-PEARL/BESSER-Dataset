





import java.util.List;
import java.util.ArrayList;

public class scxml_If  {

    private String cond;





    private List<scxml_Assign> scxml_assigns;




    private List<scxml_If> scxml_ifs;


    public scxml_If(
        String cond    ) {
        this.cond = cond;
        this.scxml_assigns = new ArrayList<>();
        this.scxml_ifs = new ArrayList<>();
    }

    public scxml_If(
        String cond        ArrayList<scxml_Assign> scxml_assigns,        ArrayList<scxml_If> scxml_ifs    ) {
        this.cond = cond;
        this.scxml_assigns = scxml_assigns;
        this.scxml_ifs = scxml_ifs;
    }

    public String getCond() {
        return cond;
    }

    public void setCond(String cond) {
        this.cond = cond;
    }

    public List<scxml_Assign> getScxml_assigns() {
        return scxml_assigns;
    }

    public void addScxml_assign(Scxml_assign scxml_assign) {
        this.scxml_assigns.add(scxml_assign);
    }
    public List<scxml_If> getScxml_ifs() {
        return scxml_ifs;
    }

    public void addScxml_if(Scxml_if scxml_if) {
        this.scxml_ifs.add(scxml_if);
    }

}