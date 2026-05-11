





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeSwitch extends HaxeExpression {






    private haxe_HaxeExpression haxe_haxeexpression;




    private List<haxe_HaxeExpression> haxe_haxeexpressions;


    public haxe_HaxeSwitch(
    ) {
        super(
        );
        this.haxe_haxeexpressions = new ArrayList<>();
    }

    public haxe_HaxeSwitch(
        ArrayList<haxe_HaxeExpression> haxe_haxeexpressions    ) {
        this.haxe_haxeexpressions = haxe_haxeexpressions;
    }


    public haxe_HaxeExpression getHaxe_haxeexpression() {
        return haxe_haxeexpression;
    }

    public void setHaxe_haxeexpression(haxe_HaxeExpression haxe_haxeexpression) {
        this.haxe_haxeexpression = haxe_haxeexpression;
    }
    public List<haxe_HaxeExpression> getHaxe_haxeexpressions() {
        return haxe_haxeexpressions;
    }

    public void addHaxe_haxeexpression(Haxe_haxeexpression haxe_haxeexpression) {
        this.haxe_haxeexpressions.add(haxe_haxeexpression);
    }

}