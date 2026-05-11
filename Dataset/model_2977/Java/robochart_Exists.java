





import java.util.List;
import java.util.ArrayList;

public class robochart_Exists extends QuantifierExpression {

    private boolean unique;



    public robochart_Exists(
        boolean unique    ) {
        super(
        );
        this.unique = unique;
    }


    public boolean getUnique() {
        return unique;
    }

    public void setUnique(boolean unique) {
        this.unique = unique;
    }


}