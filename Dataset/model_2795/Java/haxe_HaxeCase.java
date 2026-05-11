





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeCase extends HaxeExpression {






    private List<haxe_HaxeExpression> haxe_haxeexpressions;




    private haxe_HaxeSwitch haxe_haxeswitch;




    private haxe_HaxeExpression haxe_haxeexpression;


    public haxe_HaxeCase(
    ) {
        super(
        );
        this.haxe_haxeexpressions = new ArrayList<>();
    }

    public haxe_HaxeCase(
        ArrayList<haxe_HaxeExpression> haxe_haxeexpressions    ) {
        this.haxe_haxeexpressions = haxe_haxeexpressions;
    }


    public List<haxe_HaxeExpression> getHaxe_haxeexpressions() {
        return haxe_haxeexpressions;
    }

    public void addHaxe_haxeexpression(Haxe_haxeexpression haxe_haxeexpression) {
        this.haxe_haxeexpressions.add(haxe_haxeexpression);
    }
    public haxe_HaxeSwitch getHaxe_haxeswitch() {
        return haxe_haxeswitch;
    }

    public void setHaxe_haxeswitch(haxe_HaxeSwitch haxe_haxeswitch) {
        this.haxe_haxeswitch = haxe_haxeswitch;
    }
    public haxe_HaxeExpression getHaxe_haxeexpression() {
        return haxe_haxeexpression;
    }

    public void setHaxe_haxeexpression(haxe_HaxeExpression haxe_haxeexpression) {
        this.haxe_haxeexpression = haxe_haxeexpression;
    }

}