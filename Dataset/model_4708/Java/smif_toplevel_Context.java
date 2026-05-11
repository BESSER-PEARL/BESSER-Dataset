





import java.util.List;
import java.util.ArrayList;

public class smif_toplevel_Context extends IdentifiableEntity {






    private List<ExpressionContext> expressioncontexts;




    private List<Thing> things;


    public smif_toplevel_Context(
    ) {
        super(
        );
        this.expressioncontexts = new ArrayList<>();
        this.things = new ArrayList<>();
    }

    public smif_toplevel_Context(
        ArrayList<ExpressionContext> expressioncontexts,        ArrayList<Thing> things    ) {
        this.expressioncontexts = expressioncontexts;
        this.things = things;
    }


    public List<ExpressionContext> getExpressioncontexts() {
        return expressioncontexts;
    }

    public void addExpressioncontext(Expressioncontext expressioncontext) {
        this.expressioncontexts.add(expressioncontext);
    }
    public List<Thing> getThings() {
        return things;
    }

    public void addThing(Thing thing) {
        this.things.add(thing);
    }

}