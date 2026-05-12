





import java.util.List;
import java.util.ArrayList;

public class statechart_CompositeState extends State {

    private boolean isConcurrent;





    private statechart_StateVertex statechart_statevertex;




    private List<statechart_StateVertex> statechart_statevertexs;


    public statechart_CompositeState(
        boolean isConcurrent    ) {
        super(
        );
        this.isConcurrent = isConcurrent;
        this.statechart_statevertexs = new ArrayList<>();
    }

    public statechart_CompositeState(
        boolean isConcurrent        ArrayList<statechart_StateVertex> statechart_statevertexs    ) {
        this.isConcurrent = isConcurrent;
        this.statechart_statevertexs = statechart_statevertexs;
    }

    public boolean getIsconcurrent() {
        return isConcurrent;
    }

    public void setIsconcurrent(boolean isConcurrent) {
        this.isConcurrent = isConcurrent;
    }

    public statechart_StateVertex getStatechart_statevertex() {
        return statechart_statevertex;
    }

    public void setStatechart_statevertex(statechart_StateVertex statechart_statevertex) {
        this.statechart_statevertex = statechart_statevertex;
    }
    public List<statechart_StateVertex> getStatechart_statevertexs() {
        return statechart_statevertexs;
    }

    public void addStatechart_statevertex(Statechart_statevertex statechart_statevertex) {
        this.statechart_statevertexs.add(statechart_statevertex);
    }

}