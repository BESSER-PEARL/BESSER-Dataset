





import java.util.List;
import java.util.ArrayList;

public class DOM_Modifier extends ExtendedModifier, ASTNode {

    private String none;
    private String final;
    private String private;
    private String synchronized;
    private String native;
    private String static;
    private String transient;
    private String volatile;
    private String public;
    private String abstract;
    private String strictfp;
    private String protected;



    public DOM_Modifier(
        String none,        String final,        String private,        String synchronized,        String native,        String static,        String transient,        String volatile,        String public,        String abstract,        String strictfp,        String protected    ) {
        super(
        );
        this.none = none;
        this.final = final;
        this.private = private;
        this.synchronized = synchronized;
        this.native = native;
        this.static = static;
        this.transient = transient;
        this.volatile = volatile;
        this.public = public;
        this.abstract = abstract;
        this.strictfp = strictfp;
        this.protected = protected;
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
    public String getPrivate() {
        return private;
    }

    public void setPrivate(String private) {
        this.private = private;
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
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getPublic() {
        return public;
    }

    public void setPublic(String public) {
        this.public = public;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(String strictfp) {
        this.strictfp = strictfp;
    }
    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
    }


}