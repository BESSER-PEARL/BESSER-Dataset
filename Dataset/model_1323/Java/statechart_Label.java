





import java.util.List;
import java.util.ArrayList;

public class statechart_Label extends IDBase {

    private String name;





    private statechart_StateVertex statechart_statevertex;


    public statechart_Label(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public statechart_StateVertex getStatechart_statevertex() {
        return statechart_statevertex;
    }

    public void setStatechart_statevertex(statechart_StateVertex statechart_statevertex) {
        this.statechart_statevertex = statechart_statevertex;
    }

}