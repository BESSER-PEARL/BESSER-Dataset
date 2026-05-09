





import java.util.List;
import java.util.ArrayList;

public class DOM_Modifier extends ExtendedModifier, ASTNode {

    private String public;
    private String synchronized;
    private String protected;
    private String strictfp;
    private String private;
    private String final;
    private String none;
    private String native;
    private String volatile;
    private String abstract;
    private String transient;
    private String static;



    public DOM_Modifier(
        String public,        String synchronized,        String protected,        String strictfp,        String private,        String final,        String none,        String native,        String volatile,        String abstract,        String transient,        String static    ) {
        super(
        );
        this.public = public;
        this.synchronized = synchronized;
        this.protected = protected;
        this.strictfp = strictfp;
        this.private = private;
        this.final = final;
        this.none = none;
        this.native = native;
        this.volatile = volatile;
        this.abstract = abstract;
        this.transient = transient;
        this.static = static;
    }


    public String getPublic() {
        return public;
    }

    public void setPublic(String public) {
        this.public = public;
    }
    public String getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(String synchronized) {
        this.synchronized = synchronized;
    }
    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
    }
    public String getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(String strictfp) {
        this.strictfp = strictfp;
    }
    public String getPrivate() {
        return private;
    }

    public void setPrivate(String private) {
        this.private = private;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getNone() {
        return none;
    }

    public void setNone(String none) {
        this.none = none;
    }
    public String getNative() {
        return native;
    }

    public void setNative(String native) {
        this.native = native;
    }
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }


}