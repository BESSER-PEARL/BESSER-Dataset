





import java.util.List;
import java.util.ArrayList;

public class imperativeocl_TryExp extends ImperativeExpression {






    private List<imperativeocl_CatchExp> imperativeocl_catchexps;


    public imperativeocl_TryExp(
    ) {
        super(
        );
        this.imperativeocl_catchexps = new ArrayList<>();
    }

    public imperativeocl_TryExp(
        ArrayList<imperativeocl_CatchExp> imperativeocl_catchexps    ) {
        this.imperativeocl_catchexps = imperativeocl_catchexps;
    }


    public List<imperativeocl_CatchExp> getImperativeocl_catchexps() {
        return imperativeocl_catchexps;
    }

    public void addImperativeocl_catchexp(Imperativeocl_catchexp imperativeocl_catchexp) {
        this.imperativeocl_catchexps.add(imperativeocl_catchexp);
    }

}