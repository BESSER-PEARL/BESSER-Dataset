





import java.util.List;
import java.util.ArrayList;

public class mutatorenvironment_miniOCL_RoundedBracketClauseCS  {






    private List<ExpCS> expcss;


    public mutatorenvironment_miniOCL_RoundedBracketClauseCS(
    ) {
        this.expcss = new ArrayList<>();
    }

    public mutatorenvironment_miniOCL_RoundedBracketClauseCS(
        ArrayList<ExpCS> expcss    ) {
        this.expcss = expcss;
    }


    public List<ExpCS> getExpcss() {
        return expcss;
    }

    public void addExpcs(Expcs expcs) {
        this.expcss.add(expcs);
    }

}