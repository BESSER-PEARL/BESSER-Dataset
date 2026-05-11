





import java.util.List;
import java.util.ArrayList;

public class basicFsmEnv_Machine  {

    private String name;





    private List<basicFsmEnv_Trans> basicfsmenv_transs;




    private List<basicFsmEnv_State> basicfsmenv_states;


    public basicFsmEnv_Machine(
        String name    ) {
        this.name = name;
        this.basicfsmenv_transs = new ArrayList<>();
        this.basicfsmenv_states = new ArrayList<>();
    }

    public basicFsmEnv_Machine(
        String name        ArrayList<basicFsmEnv_Trans> basicfsmenv_transs,        ArrayList<basicFsmEnv_State> basicfsmenv_states    ) {
        this.name = name;
        this.basicfsmenv_transs = basicfsmenv_transs;
        this.basicfsmenv_states = basicfsmenv_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<basicFsmEnv_Trans> getBasicfsmenv_transs() {
        return basicfsmenv_transs;
    }

    public void addBasicfsmenv_trans(Basicfsmenv_trans basicfsmenv_trans) {
        this.basicfsmenv_transs.add(basicfsmenv_trans);
    }
    public List<basicFsmEnv_State> getBasicfsmenv_states() {
        return basicfsmenv_states;
    }

    public void addBasicfsmenv_state(Basicfsmenv_state basicfsmenv_state) {
        this.basicfsmenv_states.add(basicfsmenv_state);
    }

}