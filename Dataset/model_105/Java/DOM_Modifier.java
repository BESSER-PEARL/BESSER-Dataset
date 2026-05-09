





import java.util.List;
import java.util.ArrayList;

public class DOM_Modifier extends ExtendedModifier, ASTNode {

    private String native;
    private String protected;
    private String static;
    private String none;
    private String transient;
    private String public;
    private String abstract;
    private String synchronized;
    private String private;
    private String volatile;
    private String strictfp;
    private String final;



    public DOM_Modifier(
        String native,        String protected,        String static,        String none,        String transient,        String public,        String abstract,        String synchronized,        String private,        String volatile,        String strictfp,        String final    ) {
        super(
        );
        this.native = native;
        this.protected = protected;
        this.static = static;
        this.none = none;
        this.transient = transient;
        this.public = public;
        this.abstract = abstract;
        this.synchronized = synchronized;
        this.private = private;
        this.volatile = volatile;
        this.strictfp = strictfp;
        this.final = final;
    }


    public String getNative() {
        return native;
    }

    public void setNative(String native) {
        this.native = native;
    }
    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getNone() {
        return none;
    }

    public void setNone(String none) {
        this.none = none;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
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
    public String getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(String synchronized) {
        this.synchronized = synchronized;
    }
    public String getPrivate() {
        return private;
    }

    public void setPrivate(String private) {
        this.private = private;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(String strictfp) {
        this.strictfp = strictfp;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }


}