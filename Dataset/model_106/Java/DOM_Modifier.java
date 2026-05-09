





import java.util.List;
import java.util.ArrayList;

public class DOM_Modifier extends ASTNode, ExtendedModifier {

    private String private;
    private String volatile;
    private String synchronized;
    private String protected;
    private String native;
    private String static;
    private String strictfp;
    private String abstract;
    private String none;
    private String public;
    private String final;
    private String transient;



    public DOM_Modifier(
        String private,        String volatile,        String synchronized,        String protected,        String native,        String static,        String strictfp,        String abstract,        String none,        String public,        String final,        String transient    ) {
        super(
        );
        this.private = private;
        this.volatile = volatile;
        this.synchronized = synchronized;
        this.protected = protected;
        this.native = native;
        this.static = static;
        this.strictfp = strictfp;
        this.abstract = abstract;
        this.none = none;
        this.public = public;
        this.final = final;
        this.transient = transient;
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
    public String getNone() {
        return none;
    }

    public void setNone(String none) {
        this.none = none;
    }
    public String getPublic() {
        return public;
    }

    public void setPublic(String public) {
        this.public = public;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getTransient() {
        return transient;
    }

    public void setTransient(String transient) {
        this.transient = transient;
    }


}