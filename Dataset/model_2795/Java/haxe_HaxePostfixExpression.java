





import java.util.List;
import java.util.ArrayList;

public class haxe_HaxePostfixExpression extends HaxeUnaryExpression {

    private boolean isIncrement;



    public haxe_HaxePostfixExpression(
        boolean isIncrement    ) {
        super(
        );
        this.isIncrement = isIncrement;
    }


    public boolean getIsincrement() {
        return isIncrement;
    }

    public void setIsincrement(boolean isIncrement) {
        this.isIncrement = isIncrement;
    }


}