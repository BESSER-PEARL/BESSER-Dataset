





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeBlock extends HaxeExpression {






    private List<haxe_HaxeExpression> haxe_haxeexpressions;


    public haxe_HaxeBlock(
    ) {
        super(
        );
        this.haxe_haxeexpressions = new ArrayList<>();
    }

    public haxe_HaxeBlock(
        ArrayList<haxe_HaxeExpression> haxe_haxeexpressions    ) {
        this.haxe_haxeexpressions = haxe_haxeexpressions;
    }


    public List<haxe_HaxeExpression> getHaxe_haxeexpressions() {
        return haxe_haxeexpressions;
    }

    public void addHaxe_haxeexpression(Haxe_haxeexpression haxe_haxeexpression) {
        this.haxe_haxeexpressions.add(haxe_haxeexpression);
    }

}