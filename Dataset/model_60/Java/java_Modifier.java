





import java.util.List;
import java.util.ArrayList;

public class java_Modifier extends ASTNode {

    private boolean native;
    private String inheritance;
    private String visibility;
    private boolean strictfp;
    private boolean static;
    private boolean synchronized;
    private boolean transient;
    private boolean volatile;



    public java_Modifier(
        boolean native,        String inheritance,        String visibility,        boolean strictfp,        boolean static,        boolean synchronized,        boolean transient,        boolean volatile    ) {
        super(
        );
        this.native = native;
        this.inheritance = inheritance;
        this.visibility = visibility;
        this.strictfp = strictfp;
        this.static = static;
        this.synchronized = synchronized;
        this.transient = transient;
        this.volatile = volatile;
    }


    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
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
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
    }
    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
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


}