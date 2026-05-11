





import java.util.List;
import java.util.ArrayList;

public class lts_LTS  {

    private String name;





    private lts_InitialState lts_initialstate;




    private lts_FinalState lts_finalstate;




    private List<lts_IntermediateState> lts_intermediatestates;


    public lts_LTS(
        String name    ) {
        this.name = name;
        this.lts_intermediatestates = new ArrayList<>();
    }

    public lts_LTS(
        String name        ArrayList<lts_IntermediateState> lts_intermediatestates    ) {
        this.name = name;
        this.lts_intermediatestates = lts_intermediatestates;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public lts_InitialState getLts_initialstate() {
        return lts_initialstate;
    }

    public void setLts_initialstate(lts_InitialState lts_initialstate) {
        this.lts_initialstate = lts_initialstate;
    }
    public lts_FinalState getLts_finalstate() {
        return lts_finalstate;
    }

    public void setLts_finalstate(lts_FinalState lts_finalstate) {
        this.lts_finalstate = lts_finalstate;
    }
    public List<lts_IntermediateState> getLts_intermediatestates() {
        return lts_intermediatestates;
    }

    public void addLts_intermediatestate(Lts_intermediatestate lts_intermediatestate) {
        this.lts_intermediatestates.add(lts_intermediatestate);
    }

}