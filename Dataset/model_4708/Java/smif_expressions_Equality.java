





import java.util.List;
import java.util.ArrayList;

public class smif_expressions_Equality extends ExpressionNode {






    private List<Thing> things;


    public smif_expressions_Equality(
    ) {
        super(
        );
        this.things = new ArrayList<>();
    }

    public smif_expressions_Equality(
        ArrayList<Thing> things    ) {
        this.things = things;
    }


    public List<Thing> getThings() {
        return things;
    }

    public void addThing(Thing thing) {
        this.things.add(thing);
    }

}