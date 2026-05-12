





import java.util.List;
import java.util.ArrayList;

public class luniferadoc_richstring_RichStringTable extends RichStringMarkup {






    private List<richstring_luniferadoc_XExpression> richstring_luniferadoc_xexpressions;


    public luniferadoc_richstring_RichStringTable(
    ) {
        super(
        );
        this.richstring_luniferadoc_xexpressions = new ArrayList<>();
    }

    public luniferadoc_richstring_RichStringTable(
        ArrayList<richstring_luniferadoc_XExpression> richstring_luniferadoc_xexpressions    ) {
        this.richstring_luniferadoc_xexpressions = richstring_luniferadoc_xexpressions;
    }


    public List<richstring_luniferadoc_XExpression> getRichstring_luniferadoc_xexpressions() {
        return richstring_luniferadoc_xexpressions;
    }

    public void addRichstring_luniferadoc_xexpression(Richstring_luniferadoc_xexpression richstring_luniferadoc_xexpression) {
        this.richstring_luniferadoc_xexpressions.add(richstring_luniferadoc_xexpression);
    }

}