





import java.util.List;
import java.util.ArrayList;

public class basicfsm_Machine  {

    private String name;





    private List<basicfsm_Trans> basicfsm_transs;


    public basicfsm_Machine(
        String name    ) {
        this.name = name;
        this.basicfsm_transs = new ArrayList<>();
    }

    public basicfsm_Machine(
        String name        ArrayList<basicfsm_Trans> basicfsm_transs    ) {
        this.name = name;
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

}