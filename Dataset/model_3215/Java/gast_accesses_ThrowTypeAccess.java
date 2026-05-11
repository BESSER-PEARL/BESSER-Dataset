





import java.util.List;
import java.util.ArrayList;

public class gast_accesses_ThrowTypeAccess extends TypeAccess {

    private boolean declared;



    public gast_accesses_ThrowTypeAccess(
        boolean declared    ) {
        super(
        );
        this.declared = declared;
    }


    public boolean getDeclared() {
        return declared;
    }

    public void setDeclared(boolean declared) {
        this.declared = declared;
    }


}