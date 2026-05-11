





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeArrayCreation extends HaxeExpression {






    private List<haxe_HaxeExpression> haxe_haxeexpressions;


    public haxe_HaxeArrayCreation(
    ) {
        super(
        );
        this.haxe_haxeexpressions = new ArrayList<>();
    }

    public haxe_HaxeArrayCreation(
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