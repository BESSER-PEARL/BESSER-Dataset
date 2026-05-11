





import java.util.List;
import java.util.ArrayList;

public class gast_functions_Constructor extends types_Member, functions_Function {

    private boolean initializer;





    private GASTClass gastclass;


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

    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }

}