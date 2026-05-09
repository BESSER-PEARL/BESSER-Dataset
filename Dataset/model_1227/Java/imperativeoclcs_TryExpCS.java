





import java.util.List;
import java.util.ArrayList;

public class imperativeoclcs_TryExpCS extends ExpressionBlockCS {






    private List<imperativeoclcs_ExceptCS> imperativeoclcs_exceptcss;


    public imperativeoclcs_TryExpCS(
    ) {
        super(
        );
        this.imperativeoclcs_exceptcss = new ArrayList<>();
    }

    public imperativeoclcs_TryExpCS(
        ArrayList<imperativeoclcs_ExceptCS> imperativeoclcs_exceptcss    ) {
        this.imperativeoclcs_exceptcss = imperativeoclcs_exceptcss;
    }


    public List<imperativeoclcs_ExceptCS> getImperativeoclcs_exceptcss() {
        return imperativeoclcs_exceptcss;
    }

    public void addImperativeoclcs_exceptcs(Imperativeoclcs_exceptcs imperativeoclcs_exceptcs) {
        this.imperativeoclcs_exceptcss.add(imperativeoclcs_exceptcs);
    }

}