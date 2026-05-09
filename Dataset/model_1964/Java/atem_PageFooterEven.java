





import java.util.List;
import java.util.ArrayList;

public class atem_PageFooterEven extends HeadComponent {






    private List<atem_HeaderFooterColumn> atem_headerfootercolumns;


    public atem_PageFooterEven(
    ) {
        super(
        );
        this.atem_headerfootercolumns = new ArrayList<>();
    }

    public atem_PageFooterEven(
        ArrayList<atem_HeaderFooterColumn> atem_headerfootercolumns    ) {
        this.atem_headerfootercolumns = atem_headerfootercolumns;
    }


    public List<atem_HeaderFooterColumn> getAtem_headerfootercolumns() {
        return atem_headerfootercolumns;
    }

    public void addAtem_headerfootercolumn(Atem_headerfootercolumn atem_headerfootercolumn) {
        this.atem_headerfootercolumns.add(atem_headerfootercolumn);
    }

}