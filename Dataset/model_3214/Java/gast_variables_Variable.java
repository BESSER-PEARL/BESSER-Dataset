





import java.util.List;
import java.util.ArrayList;

public class gast_variables_Variable extends core_NamedModelElement, core_SourceEntity {

    private boolean const;





    private GASTType gasttype;


    public gast_variables_Variable(
        boolean const    ) {
        super(
        );
        this.const = const;
    }


    public boolean getConst() {
        return const;
    }

    public void setConst(boolean const) {
        this.const = const;
    }

    public GASTType getGasttype() {
        return gasttype;
    }

    public void setGasttype(GASTType gasttype) {
        this.gasttype = gasttype;
    }

}