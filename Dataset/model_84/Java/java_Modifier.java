





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private boolean strictfp;
    private boolean transient;
    private boolean synchronized;
    private boolean native;
    private boolean volatile;
    private boolean static;
    private String inheritance;
    private String visibility;



    public java_Modifier(
        boolean strictfp,        boolean transient,        boolean synchronized,        boolean native,        boolean volatile,        boolean static,        String inheritance,        String visibility    ) {
        super(
        );
        this.strictfp = strictfp;
        this.transient = transient;
        this.synchronized = synchronized;
        this.native = native;
        this.volatile = volatile;
        this.static = static;
        this.inheritance = inheritance;
        this.visibility = visibility;
    }


    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
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
    public String getInheritance() {
        return inheritance;
    }

    public void setInheritance(String inheritance) {
        this.inheritance = inheritance;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }


}