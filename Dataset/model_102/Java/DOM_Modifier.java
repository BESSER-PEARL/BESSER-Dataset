





import java.util.List;
import java.util.ArrayList;

public class DOM_Modifier extends ASTNode, ExtendedModifier {

    private String final;
    private String synchronized;
    private String abstract;
    private String strictfp;
    private String protected;
    private String transient;
    private String none;
    private String public;
    private String native;
    private String volatile;
    private String private;
    private String static;



    public DOM_Modifier(
        String final,        String synchronized,        String abstract,        String strictfp,        String protected,        String transient,        String none,        String public,        String native,        String volatile,        String private,        String static    ) {
        super(
        );
        this.final = final;
        this.synchronized = synchronized;
        this.abstract = abstract;
        this.strictfp = strictfp;
        this.protected = protected;
        this.transient = transient;
        this.none = none;
        this.public = public;
        this.native = native;
        this.volatile = volatile;
        this.private = private;
        this.static = static;
    }


    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(String synchronized) {
        this.synchronized = synchronized;
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
    public String getPublic() {
        return public;
    }

    public void setPublic(String public) {
        this.public = public;
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


}