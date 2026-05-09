





import java.util.List;
import java.util.ArrayList;

public class atem_HeaderFooterColumn  {






    private atem_PageHeaderEven atem_pageheadereven;




    private List<atem_HeaderFooterFragment> atem_headerfooterfragments;


    public atem_HeaderFooterColumn(
    ) {
        this.atem_headerfooterfragments = new ArrayList<>();
    }

    public atem_HeaderFooterColumn(
        ArrayList<atem_HeaderFooterFragment> atem_headerfooterfragments    ) {
        this.atem_headerfooterfragments = atem_headerfooterfragments;
    }


    public atem_PageHeaderEven getAtem_pageheadereven() {
        return atem_pageheadereven;
    }

    public void setAtem_pageheadereven(atem_PageHeaderEven atem_pageheadereven) {
        this.atem_pageheadereven = atem_pageheadereven;
    }
    public List<atem_HeaderFooterFragment> getAtem_headerfooterfragments() {
        return atem_headerfooterfragments;
    }

    public void addAtem_headerfooterfragment(Atem_headerfooterfragment atem_headerfooterfragment) {
        this.atem_headerfooterfragments.add(atem_headerfooterfragment);
    }

}