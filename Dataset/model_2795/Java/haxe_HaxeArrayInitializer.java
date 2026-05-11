





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxeArrayInitializer extends HaxeExpression {






    private List<haxe_HaxeExpression> haxe_haxeexpressions;




    private haxe_HaxeArrayCreation haxe_haxearraycreation;


    public haxe_HaxeArrayInitializer(
    ) {
        super(
        );
        this.haxe_haxeexpressions = new ArrayList<>();
    }

    public haxe_HaxeArrayInitializer(
        ArrayList<haxe_HaxeExpression> haxe_haxeexpressions    ) {
        this.haxe_haxeexpressions = haxe_haxeexpressions;
    }


    public List<haxe_HaxeExpression> getHaxe_haxeexpressions() {
        return haxe_haxeexpressions;
    }

    public void addHaxe_haxeexpression(Haxe_haxeexpression haxe_haxeexpression) {
        this.haxe_haxeexpressions.add(haxe_haxeexpression);
    }
    public haxe_HaxeArrayCreation getHaxe_haxearraycreation() {
        return haxe_haxearraycreation;
    }

    public void setHaxe_haxearraycreation(haxe_HaxeArrayCreation haxe_haxearraycreation) {
        this.haxe_haxearraycreation = haxe_haxearraycreation;
    }

}