





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_hlpn_Transition extends hlpn_ContextVariable, hlpn_Node {






    private List<ArcPT> arcpts;




    private List<ArcTP> arctps;


    public highlevelnets_hlpn_Transition(
    ) {
        super(
        );
        this.arcpts = new ArrayList<>();
        this.arctps = new ArrayList<>();
    }

    public highlevelnets_hlpn_Transition(
        ArrayList<ArcPT> arcpts,        ArrayList<ArcTP> arctps    ) {
        this.arcpts = arcpts;
        this.arctps = arctps;
    }


    public List<ArcPT> getArcpts() {
        return arcpts;
    }

    public void addArcpt(Arcpt arcpt) {
        this.arcpts.add(arcpt);
    }
    public List<ArcTP> getArctps() {
        return arctps;
    }

    public void addArctp(Arctp arctp) {
        this.arctps.add(arctp);
    }

}