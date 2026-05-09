





import java.util.List;
import java.util.ArrayList;

public class imperativeoclcs_ExpressionBlockCS extends ExpCS {






    private List<imperativeoclcs_ExpCS> imperativeoclcs_expcss;


    public imperativeoclcs_ExpressionBlockCS(
    ) {
        super(
        );
        this.imperativeoclcs_expcss = new ArrayList<>();
    }

    public imperativeoclcs_ExpressionBlockCS(
        ArrayList<imperativeoclcs_ExpCS> imperativeoclcs_expcss    ) {
        this.imperativeoclcs_expcss = imperativeoclcs_expcss;
    }


    public List<imperativeoclcs_ExpCS> getImperativeoclcs_expcss() {
        return imperativeoclcs_expcss;
    }

    public void addImperativeoclcs_expcs(Imperativeoclcs_expcs imperativeoclcs_expcs) {
        this.imperativeoclcs_expcss.add(imperativeoclcs_expcs);
    }

}