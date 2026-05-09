





import java.util.List;
import java.util.ArrayList;

public class DOM_Modifier extends ExtendedModifier, ASTNode {

    private String private;
    private String strictfp;
    private String abstract;
    private String synchronized;
    private String final;
    private String public;
    private String static;
    private String volatile;
    private String protected;
    private String transient;
    private String native;
    private String none;



    public DOM_Modifier(
        String private,        String strictfp,        String abstract,        String synchronized,        String final,        String public,        String static,        String volatile,        String protected,        String transient,        String native,        String none    ) {
        super(
        );
        this.private = private;
        this.strictfp = strictfp;
        this.abstract = abstract;
        this.synchronized = synchronized;
        this.final = final;
        this.public = public;
        this.static = static;
        this.volatile = volatile;
        this.protected = protected;
        this.transient = transient;
        this.native = native;
        this.none = none;
    }


    public String getPrivate() {
        return private;
    }

    public void setPrivate(String private) {
        this.private = private;
    }
    public String getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(String strictfp) {
        this.strictfp = strictfp;
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
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getPublic() {
        return public;
    }

    public void setPublic(String public) {
        this.public = public;
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
    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }
    public String getNative() {
        return native;
    }

    public void setNative(String native) {
        this.native = native;
    }
    public String getNone() {
        return none;
    }

    public void setNone(String none) {
        this.none = none;
    }


}