





import java.util.List;
import java.util.ArrayList;

public class ardurobotml_Region  {

    private String name;





    private List<ardurobotml_State> ardurobotml_states;




    private ardurobotml_RegionContainer ardurobotml_regioncontainer;


    public ardurobotml_Region(
        String name    ) {
        this.name = name;
        this.ardurobotml_states = new ArrayList<>();
    }

    public ardurobotml_Region(
        String name        ArrayList<ardurobotml_State> ardurobotml_states    ) {
        this.name = name;
        this.ardurobotml_states = ardurobotml_states;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<ardurobotml_State> getArdurobotml_states() {
        return ardurobotml_states;
    }

    public void addArdurobotml_state(Ardurobotml_state ardurobotml_state) {
        this.ardurobotml_states.add(ardurobotml_state);
    }
    public ardurobotml_RegionContainer getArdurobotml_regioncontainer() {
        return ardurobotml_regioncontainer;
    }

    public void setArdurobotml_regioncontainer(ardurobotml_RegionContainer ardurobotml_regioncontainer) {
        this.ardurobotml_regioncontainer = ardurobotml_regioncontainer;
    }

}