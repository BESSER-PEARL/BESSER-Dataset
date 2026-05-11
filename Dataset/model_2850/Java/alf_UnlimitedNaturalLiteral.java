





import java.util.List;
import java.util.ArrayList;

public class alf_UnlimitedNaturalLiteral  {

    private boolean star;





    private alf_MultiplicityRange alf_multiplicityrange;




    private alf_INTEGER_LITERAL alf_integer_literal;


    public alf_UnlimitedNaturalLiteral(
        boolean star    ) {
        this.star = star;
    }


    public boolean getStar() {
        return star;
    }

    public void setStar(boolean star) {
        this.star = star;
    }

    public alf_MultiplicityRange getAlf_multiplicityrange() {
        return alf_multiplicityrange;
    }

    public void setAlf_multiplicityrange(alf_MultiplicityRange alf_multiplicityrange) {
        this.alf_multiplicityrange = alf_multiplicityrange;
    }
    public alf_INTEGER_LITERAL getAlf_integer_literal() {
        return alf_integer_literal;
    }

    public void setAlf_integer_literal(alf_INTEGER_LITERAL alf_integer_literal) {
        this.alf_integer_literal = alf_integer_literal;
    }

}