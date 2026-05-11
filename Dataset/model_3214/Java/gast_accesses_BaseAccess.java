





import java.util.List;
import java.util.ArrayList;

public class gast_accesses_BaseAccess extends SourceEntity {






    private Function function;




    private GASTClass gastclass;


    public gast_accesses_BaseAccess(
    ) {
        super(
        );
    }



    public Function getFunction() {
        return function;
    }

    public void setFunction(Function function) {
        this.function = function;
    }
    public GASTClass getGastclass() {
        return gastclass;
    }

    public void setGastclass(GASTClass gastclass) {
        this.gastclass = gastclass;
    }

}