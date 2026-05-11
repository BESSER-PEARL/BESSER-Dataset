





import java.util.List;
import java.util.ArrayList;

public class minuml1_CompositeState extends State {






    private List<minuml1_StateVertex> minuml1_statevertexs;


    public minuml1_CompositeState(
    ) {
        super(
        );
        this.minuml1_statevertexs = new ArrayList<>();
    }

    public minuml1_CompositeState(
        ArrayList<minuml1_StateVertex> minuml1_statevertexs    ) {
        this.minuml1_statevertexs = minuml1_statevertexs;
    }


    public List<minuml1_StateVertex> getMinuml1_statevertexs() {
        return minuml1_statevertexs;
    }

    public void addMinuml1_statevertex(Minuml1_statevertex minuml1_statevertex) {
        this.minuml1_statevertexs.add(minuml1_statevertex);
    }

}