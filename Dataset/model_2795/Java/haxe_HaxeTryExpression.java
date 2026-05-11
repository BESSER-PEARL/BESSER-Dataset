





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeTryExpression extends HaxeExpression {






    private haxe_HaxeExpression haxe_haxeexpression;




    private List<haxe_HaxeCatchClause> haxe_haxecatchclauses;


    public haxe_HaxeTryExpression(
    ) {
        super(
        );
        this.haxe_haxecatchclauses = new ArrayList<>();
    }

    public haxe_HaxeTryExpression(
        ArrayList<haxe_HaxeCatchClause> haxe_haxecatchclauses    ) {
        this.haxe_haxecatchclauses = haxe_haxecatchclauses;
    }


    public haxe_HaxeExpression getHaxe_haxeexpression() {
        return haxe_haxeexpression;
    }

    public void setHaxe_haxeexpression(haxe_HaxeExpression haxe_haxeexpression) {
        this.haxe_haxeexpression = haxe_haxeexpression;
    }
    public List<haxe_HaxeCatchClause> getHaxe_haxecatchclauses() {
        return haxe_haxecatchclauses;
    }

    public void addHaxe_haxecatchclause(Haxe_haxecatchclause haxe_haxecatchclause) {
        this.haxe_haxecatchclauses.add(haxe_haxecatchclause);
    }

}