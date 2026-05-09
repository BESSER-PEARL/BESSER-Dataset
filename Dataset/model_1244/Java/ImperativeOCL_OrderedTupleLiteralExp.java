





import java.util.List;
import java.util.ArrayList;

public class ImperativeOCL_OrderedTupleLiteralExp  {






    private List<OrderedTupleLiteralPart> orderedtupleliteralparts;


    public ImperativeOCL_OrderedTupleLiteralExp(
    ) {
        this.orderedtupleliteralparts = new ArrayList<>();
    }

    public ImperativeOCL_OrderedTupleLiteralExp(
        ArrayList<OrderedTupleLiteralPart> orderedtupleliteralparts    ) {
        this.orderedtupleliteralparts = orderedtupleliteralparts;
    }


    public List<OrderedTupleLiteralPart> getOrderedtupleliteralparts() {
        return orderedtupleliteralparts;
    }

    public void addOrderedtupleliteralpart(Orderedtupleliteralpart orderedtupleliteralpart) {
        this.orderedtupleliteralparts.add(orderedtupleliteralpart);
    }

}