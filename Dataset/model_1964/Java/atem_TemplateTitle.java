





import java.util.List;
import java.util.ArrayList;

public class atem_TemplateTitle extends HeadComponent {






    private List<atem_HeaderFooterFragment> atem_headerfooterfragments;


    public atem_TemplateTitle(
    ) {
        super(
        );
        this.atem_headerfooterfragments = new ArrayList<>();
    }

    public atem_TemplateTitle(
        ArrayList<atem_HeaderFooterFragment> atem_headerfooterfragments    ) {
        this.atem_headerfooterfragments = atem_headerfooterfragments;
    }


    public List<atem_HeaderFooterFragment> getAtem_headerfooterfragments() {
        return atem_headerfooterfragments;
    }

    public void addAtem_headerfooterfragment(Atem_headerfooterfragment atem_headerfooterfragment) {
        this.atem_headerfooterfragments.add(atem_headerfooterfragment);
    }

}