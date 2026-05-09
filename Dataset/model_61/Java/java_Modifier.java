





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private boolean synchronized;
    private String inheritance;
    private boolean native;
    private boolean volatile;
    private boolean static;
    private boolean transient;
    private boolean strictfp;
    private String visibility;



    public java_Modifier(
        boolean synchronized,        String inheritance,        boolean native,        boolean volatile,        boolean static,        boolean transient,        boolean strictfp,        String visibility    ) {
        super(
        );
        this.synchronized = synchronized;
        this.inheritance = inheritance;
        this.native = native;
        this.volatile = volatile;
        this.static = static;
        this.transient = transient;
        this.strictfp = strictfp;
        this.visibility = visibility;
    }


    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
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
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}