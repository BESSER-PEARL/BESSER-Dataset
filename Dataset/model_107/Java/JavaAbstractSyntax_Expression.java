





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_Expression extends ASTNode {

    private String resolveUnboxing;
    private String resolveBoxing;



    public JavaAbstractSyntax_Expression(
        String resolveUnboxing,        String resolveBoxing    ) {
        super(
        );
        this.resolveUnboxing = resolveUnboxing;
        this.resolveBoxing = resolveBoxing;
    }


    public String getResolveunboxing() {
        return resolveUnboxing;
    }

    public void setResolveunboxing(String resolveUnboxing) {
        this.resolveUnboxing = resolveUnboxing;
    }
    public String getResolveboxing() {
        return resolveBoxing;
    }

    public void setResolveboxing(String resolveBoxing) {
        this.resolveBoxing = resolveBoxing;
    }


}