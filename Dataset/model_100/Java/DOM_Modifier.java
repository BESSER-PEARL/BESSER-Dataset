





import java.util.List;
import java.util.ArrayList;

public class DOM_Modifier extends ASTNode, ExtendedModifier {

    private String final;
    private String private;
    private String protected;
    private String abstract;
    private String synchronized;
    private String volatile;
    private String static;
    private String transient;
    private String none;
    private String native;
    private String public;
    private String strictfp;



    public DOM_Modifier(
        String final,        String private,        String protected,        String abstract,        String synchronized,        String volatile,        String static,        String transient,        String none,        String native,        String public,        String strictfp    ) {
        super(
        );
        this.final = final;
        this.private = private;
        this.protected = protected;
        this.abstract = abstract;
        this.synchronized = synchronized;
        this.volatile = volatile;
        this.static = static;
        this.transient = transient;
        this.none = none;
        this.native = native;
        this.public = public;
        this.strictfp = strictfp;
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
    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
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
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
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


}