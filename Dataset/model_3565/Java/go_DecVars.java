





import java.util.List;
import java.util.ArrayList;

public class go_DecVars  {

    private String vars;





    private List<go_Atrib_Aux> go_atrib_auxs;


    public go_DecVars(
        String vars    ) {
        this.vars = vars;
        this.go_atrib_auxs = new ArrayList<>();
    }

    public go_DecVars(
        String vars        ArrayList<go_Atrib_Aux> go_atrib_auxs    ) {
        this.vars = vars;
        this.go_atrib_auxs = go_atrib_auxs;
    }

    public String getVars() {
        return vars;
    }

    public void setVars(String vars) {
        this.vars = vars;
    }

    public List<go_Atrib_Aux> getGo_atrib_auxs() {
        return go_atrib_auxs;
    }

    public void addGo_atrib_aux(Go_atrib_aux go_atrib_aux) {
        this.go_atrib_auxs.add(go_atrib_aux);
    }

}