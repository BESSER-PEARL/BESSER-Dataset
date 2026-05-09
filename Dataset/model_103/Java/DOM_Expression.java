





import java.util.List;
import java.util.ArrayList;

public class DOM_Expression extends ASTNode {

    private String resolveBoxing;
    private String resolveUnboxing;





    private IType itype;


    public DOM_Expression(
        String resolveBoxing,        String resolveUnboxing    ) {
        super(
        );
        this.resolveBoxing = resolveBoxing;
        this.resolveUnboxing = resolveUnboxing;
    }


    public String getResolveboxing() {
        return resolveBoxing;
    }

    public void setResolveboxing(String resolveBoxing) {
        this.resolveBoxing = resolveBoxing;
    }
    public String getResolveunboxing() {
        return resolveUnboxing;
    }

    public void setResolveunboxing(String resolveUnboxing) {
        this.resolveUnboxing = resolveUnboxing;
    }

    public IType getItype() {
        return itype;
    }

    public void setItype(IType itype) {
        this.itype = itype;
    }

}