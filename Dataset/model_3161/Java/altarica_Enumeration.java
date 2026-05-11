





import java.util.List;
import java.util.ArrayList;

public class altarica_Enumeration extends AbstractDomain {






    private List<altarica_Literal> altarica_literals;


    public altarica_Enumeration(
    ) {
        super(
        );
        this.altarica_literals = new ArrayList<>();
    }

    public altarica_Enumeration(
        ArrayList<altarica_Literal> altarica_literals    ) {
        this.altarica_literals = altarica_literals;
    }


    public List<altarica_Literal> getAltarica_literals() {
        return altarica_literals;
    }

    public void addAltarica_literal(Altarica_literal altarica_literal) {
        this.altarica_literals.add(altarica_literal);
    }

}