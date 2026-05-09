





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_Modifier extends ExtendedModifier, ASTNode {

    private String synchronized;
    private String private;
    private String native;
    private String public;
    private String final;
    private String volatile;
    private String abstract;
    private String none;
    private String strictfp;
    private String transient;
    private String static;
    private String protected;



    public JavaAbstractSyntax_Modifier(
        String synchronized,        String private,        String native,        String public,        String final,        String volatile,        String abstract,        String none,        String strictfp,        String transient,        String static,        String protected    ) {
        super(
        );
        this.synchronized = synchronized;
        this.private = private;
        this.native = native;
        this.public = public;
        this.final = final;
        this.volatile = volatile;
        this.abstract = abstract;
        this.none = none;
        this.strictfp = strictfp;
        this.transient = transient;
        this.static = static;
        this.protected = protected;
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
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
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
    public String getNone() {
        return none;
    }

    public void setNone(String none) {
        this.none = none;
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
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }
    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
    }


}