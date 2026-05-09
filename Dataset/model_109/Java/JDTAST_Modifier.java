





import java.util.List;
import java.util.ArrayList;

public class JDTAST_Modifier extends ASTNode, ExtendedModifier {

    private String private;
    private String native;
    private String abstract;
    private String final;
    private String protected;
    private String volatile;
    private String synchronized;
    private String none;
    private String transient;
    private String public;
    private String strictfp;
    private String static;



    public JDTAST_Modifier(
        String private,        String native,        String abstract,        String final,        String protected,        String volatile,        String synchronized,        String none,        String transient,        String public,        String strictfp,        String static    ) {
        super(
        );
        this.private = private;
        this.native = native;
        this.abstract = abstract;
        this.final = final;
        this.protected = protected;
        this.volatile = volatile;
        this.synchronized = synchronized;
        this.none = none;
        this.transient = transient;
        this.public = public;
        this.strictfp = strictfp;
        this.static = static;
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
    public String getAbstract() {
        return abstract;
    }

    public void setAbstract(String abstract) {
        this.abstract = abstract;
    }
    public String getFinal() {
        return final;
    }

    public void setFinal(String final) {
        this.final = final;
    }
    public String getProtected() {
        return protected;
    }

    public void setProtected(String protected) {
        this.protected = protected;
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
    public String getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(String strictfp) {
        this.strictfp = strictfp;
    }
    public String getStatic() {
        return static;
    }

    public void setStatic(String static) {
        this.static = static;
    }


}