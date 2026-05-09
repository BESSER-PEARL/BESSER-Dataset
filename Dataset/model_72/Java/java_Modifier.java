





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private String visibility;
    private boolean static;
    private boolean transient;
    private boolean volatile;
    private boolean synchronized;
    private boolean native;
    private boolean strictfp;
    private String inheritance;



    public java_Modifier(
        String visibility,        boolean static,        boolean transient,        boolean volatile,        boolean synchronized,        boolean native,        boolean strictfp,        String inheritance    ) {
        super(
        );
        this.visibility = visibility;
        this.static = static;
        this.transient = transient;
        this.volatile = volatile;
        this.synchronized = synchronized;
        this.native = native;
        this.strictfp = strictfp;
        this.inheritance = inheritance;
    }


    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
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


}