





import java.util.List;
import java.util.ArrayList;

public class eol_AnyType extends Type {

    private boolean declared;



    public eol_AnyType(
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