





import java.util.List;
import java.util.ArrayList;

public class dg_Path extends MarkedElement {






    private List<dg_PathCommand> dg_pathcommands;


    public dg_Path(
    ) {
        super(
        );
        this.dg_pathcommands = new ArrayList<>();
    }

    public dg_Path(
        ArrayList<dg_PathCommand> dg_pathcommands    ) {
        this.dg_pathcommands = dg_pathcommands;
    }


    public List<dg_PathCommand> getDg_pathcommands() {
        return dg_pathcommands;
    }

    public void addDg_pathcommand(Dg_pathcommand dg_pathcommand) {
        this.dg_pathcommands.add(dg_pathcommand);
    }

}