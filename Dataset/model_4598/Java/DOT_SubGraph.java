





import java.util.List;
import java.util.ArrayList;

public class DOT_SubGraph extends Nodelike {

    private String labelloc;





    private DOT_Nodelike dot_nodelike;




    private List<DOT_Nodelike> dot_nodelikes;


    public DOT_SubGraph(
        String labelloc    ) {
        super(
        );
        this.labelloc = labelloc;
        this.dot_nodelikes = new ArrayList<>();
    }

    public DOT_SubGraph(
        String labelloc        ArrayList<DOT_Nodelike> dot_nodelikes    ) {
        this.labelloc = labelloc;
        this.dot_nodelikes = dot_nodelikes;
    }

    public String getLabelloc() {
        return labelloc;
    }

    public void setLabelloc(String labelloc) {
        this.labelloc = labelloc;
    }

    public DOT_Nodelike getDot_nodelike() {
        return dot_nodelike;
    }

    public void setDot_nodelike(DOT_Nodelike dot_nodelike) {
        this.dot_nodelike = dot_nodelike;
    }
    public List<DOT_Nodelike> getDot_nodelikes() {
        return dot_nodelikes;
    }

    public void addDot_nodelike(Dot_nodelike dot_nodelike) {
        this.dot_nodelikes.add(dot_nodelike);
    }

}