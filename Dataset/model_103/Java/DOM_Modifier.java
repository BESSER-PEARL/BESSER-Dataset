





import java.util.List;
import java.util.ArrayList;

public class DOM_Modifier extends ExtendedModifier, ASTNode {

    private String public;
    private String strictfp;
    private String transient;
    private String abstract;
    private String none;
    private String final;
    private String protected;
    private String private;
    private String static;
    private String volatile;
    private String synchronized;
    private String native;



    public DOM_Modifier(
        String public,        String strictfp,        String transient,        String abstract,        String none,        String final,        String protected,        String private,        String static,        String volatile,        String synchronized,        String native    ) {
        super(
        );
        this.public = public;
        this.strictfp = strictfp;
        this.transient = transient;
        this.abstract = abstract;
        this.none = none;
        this.final = final;
        this.protected = protected;
        this.private = private;
        this.static = static;
        this.volatile = volatile;
        this.synchronized = synchronized;
        this.native = native;
    }


    public String getPublic() {
        return public;
    }

    public void setPublic(String public) {
        this.public = public;
    }
    public String getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(String strictfp) {
        this.strictfp = strictfp;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getNone() {
        return none;
    }

    public void setNone(String none) {
        this.none = none;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
    }
    public String getPrivate() {
        return private;
    }

    public void setPrivate(String private) {
        this.private = private;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(String synchronized) {
        this.synchronized = synchronized;
    }
    public String getNative() {
        return native;
    }

    public void setNative(String native) {
        this.native = native;
    }


}