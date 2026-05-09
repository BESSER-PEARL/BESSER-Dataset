





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private boolean strictfp;
    private String inheritance;
    private boolean transient;
    private boolean synchronized;
    private boolean volatile;
    private boolean static;
    private String visibility;
    private boolean native;



    public java_Modifier(
        boolean strictfp,        String inheritance,        boolean transient,        boolean synchronized,        boolean volatile,        boolean static,        String visibility,        boolean native    ) {
        super(
        );
        this.strictfp = strictfp;
        this.inheritance = inheritance;
        this.transient = transient;
        this.synchronized = synchronized;
        this.volatile = volatile;
        this.static = static;
        this.visibility = visibility;
        this.native = native;
    }


    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
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
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }


}