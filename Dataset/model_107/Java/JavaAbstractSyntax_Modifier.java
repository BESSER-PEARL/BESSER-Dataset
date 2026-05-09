





import java.util.List;
import java.util.ArrayList;

public class JavaAbstractSyntax_Modifier extends ASTNode, ExtendedModifier {

    private String none;
    private String abstract;
    private String protected;
    private String strictfp;
    private String native;
    private String synchronized;
    private String private;
    private String final;
    private String public;
    private String volatile;
    private String transient;
    private String static;



    public JavaAbstractSyntax_Modifier(
        String none,        String abstract,        String protected,        String strictfp,        String native,        String synchronized,        String private,        String final,        String public,        String volatile,        String transient,        String static    ) {
        super(
        );
        this.none = none;
        this.abstract = abstract;
        this.protected = protected;
        this.strictfp = strictfp;
        this.native = native;
        this.synchronized = synchronized;
        this.private = private;
        this.final = final;
        this.public = public;
        this.volatile = volatile;
        this.transient = transient;
        this.static = static;
    }


    public String getNone() {
        return none;
    }

    public void setNone(String none) {
        this.none = none;
    }
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
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
    public String getNative() {
        return native;
    }

    public void setNative(String native) {
        this.native = native;
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
    public String getVolatile() {
        return volatile;
    }

    public void setVolatile(String volatile) {
        this.volatile = volatile;
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