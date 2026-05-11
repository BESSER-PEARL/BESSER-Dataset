





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Constructor extends functions_Function, types_Member {

    private boolean initializer;



    public gast_functions_Constructor(
        boolean initializer    ) {
        super(
        );
        this.initializer = initializer;
    }


    public boolean getInitializer() {
        return initializer;
    }

    public void setInitializer(boolean initializer) {
        this.initializer = initializer;
    }


}