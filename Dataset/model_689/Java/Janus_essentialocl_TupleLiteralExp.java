





import java.util.List;
import java.util.ArrayList;

public class Janus_essentialocl_TupleLiteralExp extends LiteralExp {






    private List<TupleLiteralPart> tupleliteralparts;


    public Janus_essentialocl_TupleLiteralExp(
    ) {
        super(
        );
        this.tupleliteralparts = new ArrayList<>();
    }

    public Janus_essentialocl_TupleLiteralExp(
        ArrayList<TupleLiteralPart> tupleliteralparts    ) {
        this.tupleliteralparts = tupleliteralparts;
    }


    public List<TupleLiteralPart> getTupleliteralparts() {
        return tupleliteralparts;
    }

    public void addTupleliteralpart(Tupleliteralpart tupleliteralpart) {
        this.tupleliteralparts.add(tupleliteralpart);
    }

}