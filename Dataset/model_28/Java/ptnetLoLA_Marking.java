





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_Marking  {






    private ptnetLoLA_PtNet ptnetlola_ptnet;




    private ptnetLoLA_PtNet ptnetlola_ptnet;




    private List<ptnetLoLA_RefMarkedPlace> ptnetlola_refmarkedplaces;


    public ptnetLoLA_Marking(
    ) {
        this.ptnetlola_refmarkedplaces = new ArrayList<>();
    }

    public ptnetLoLA_Marking(
        ArrayList<ptnetLoLA_RefMarkedPlace> ptnetlola_refmarkedplaces    ) {
        this.ptnetlola_refmarkedplaces = ptnetlola_refmarkedplaces;
    }


    public ptnetLoLA_PtNet getPtnetlola_ptnet() {
        return ptnetlola_ptnet;
    }

    public void setPtnetlola_ptnet(ptnetLoLA_PtNet ptnetlola_ptnet) {
        this.ptnetlola_ptnet = ptnetlola_ptnet;
    }
    public ptnetLoLA_PtNet getPtnetlola_ptnet() {
        return ptnetlola_ptnet;
    }

    public void setPtnetlola_ptnet(ptnetLoLA_PtNet ptnetlola_ptnet) {
        this.ptnetlola_ptnet = ptnetlola_ptnet;
    }
    public List<ptnetLoLA_RefMarkedPlace> getPtnetlola_refmarkedplaces() {
        return ptnetlola_refmarkedplaces;
    }

    public void addPtnetlola_refmarkedplace(Ptnetlola_refmarkedplace ptnetlola_refmarkedplace) {
        this.ptnetlola_refmarkedplaces.add(ptnetlola_refmarkedplace);
    }

}