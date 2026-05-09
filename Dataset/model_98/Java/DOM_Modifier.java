





import java.util.List;
import java.util.ArrayList;

public class DOM_Modifier extends ASTNode, ExtendedModifier {

    private String native;
    private String protected;
    private String abstract;
    private String private;
    private String synchronized;
    private String transient;
    private String volatile;
    private String strictfp;
    private String public;
    private String static;
    private String final;
    private String none;



    public DOM_Modifier(
        String native,        String protected,        String abstract,        String private,        String synchronized,        String transient,        String volatile,        String strictfp,        String public,        String static,        String final,        String none    ) {
        super(
        );
        this.native = native;
        this.protected = protected;
        this.abstract = abstract;
        this.private = private;
        this.synchronized = synchronized;
        this.transient = transient;
        this.volatile = volatile;
        this.strictfp = strictfp;
        this.public = public;
        this.static = static;
        this.final = final;
        this.none = none;
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
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
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
    public String getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(String strictfp) {
        this.strictfp = strictfp;
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


}