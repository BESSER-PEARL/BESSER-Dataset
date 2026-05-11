





import java.util.List;
import java.util.ArrayList;

public class xs_GlobalVarDeclaration extends VarDeclaration, Declaration {

    private boolean const;
    private boolean extern;



    public xs_GlobalVarDeclaration(
        boolean const,        boolean extern    ) {
        super(
        );
        this.const = const;
        this.extern = extern;
    }


    public boolean getConst() {
        return const;
    }

    public void setConst(boolean const) {
        this.const = const;
    }
    public boolean getExtern() {
        return extern;
    }

    public void setExtern(boolean extern) {
        this.extern = extern;
    }


}