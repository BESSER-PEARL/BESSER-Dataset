





import java.util.List;
import java.util.ArrayList;

public class gast_types_Reference extends TypeDecorator {

    private boolean explicit;





    private GASTType gasttype;


    public gast_types_Reference(
        boolean explicit    ) {
        super(
        );
        this.explicit = explicit;
    }


    public boolean getExplicit() {
        return explicit;
    }

    public void setExplicit(boolean explicit) {
        this.explicit = explicit;
    }

    public GASTType getGasttype() {
        return gasttype;
    }

    public void setGasttype(GASTType gasttype) {
        this.gasttype = gasttype;
    }

}