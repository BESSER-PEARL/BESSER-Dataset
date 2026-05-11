





import java.util.List;
import java.util.ArrayList;

public class classes_Generalization extends Element {

    private boolean substitutable;



    public classes_Generalization(
        boolean substitutable    ) {
        super(
        );
        this.substitutable = substitutable;
    }


    public boolean getSubstitutable() {
        return substitutable;
    }

    public void setSubstitutable(boolean substitutable) {
        this.substitutable = substitutable;
    }


}