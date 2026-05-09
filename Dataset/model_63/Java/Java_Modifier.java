





import java.util.List;
import java.util.ArrayList;

public class Java_Modifier extends ASTNode {

    private boolean transient;
    private boolean synchronized;
    private String visibility;
    private String inheritance;
    private boolean strictfp;
    private boolean native;
    private boolean static;
    private boolean volatile;



    public Java_Modifier(
        boolean transient,        boolean synchronized,        String visibility,        String inheritance,        boolean strictfp,        boolean native,        boolean static,        boolean volatile    ) {
        super(
        );
        this.transient = transient;
        this.synchronized = synchronized;
        this.visibility = visibility;
        this.inheritance = inheritance;
        this.strictfp = strictfp;
        this.native = native;
        this.static = static;
        this.volatile = volatile;
    }


    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }


}