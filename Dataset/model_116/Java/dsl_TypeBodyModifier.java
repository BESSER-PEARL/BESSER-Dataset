





import java.util.List;
import java.util.ArrayList;

public class dsl_TypeBodyModifier  {

    private boolean volatile;
    private boolean strictfp;
    private boolean synchronized;
    private boolean transient;
    private boolean native;





    private dsl_ClassOrInterfaceBodyDeclaration dsl_classorinterfacebodydeclaration;




    private dsl_CommonModifier dsl_commonmodifier;


    public dsl_TypeBodyModifier(
        boolean volatile,        boolean strictfp,        boolean synchronized,        boolean transient,        boolean native    ) {
        this.volatile = volatile;
        this.strictfp = strictfp;
        this.synchronized = synchronized;
        this.transient = transient;
        this.native = native;
    }


    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }
    public boolean getStrictfp() {
        return strictfp;
    }

    public void setStrictfp(boolean strictfp) {
        this.strictfp = strictfp;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }

    public dsl_ClassOrInterfaceBodyDeclaration getDsl_classorinterfacebodydeclaration() {
        return dsl_classorinterfacebodydeclaration;
    }

    public void setDsl_classorinterfacebodydeclaration(dsl_ClassOrInterfaceBodyDeclaration dsl_classorinterfacebodydeclaration) {
        this.dsl_classorinterfacebodydeclaration = dsl_classorinterfacebodydeclaration;
    }
    public dsl_CommonModifier getDsl_commonmodifier() {
        return dsl_commonmodifier;
    }

    public void setDsl_commonmodifier(dsl_CommonModifier dsl_commonmodifier) {
        this.dsl_commonmodifier = dsl_commonmodifier;
    }

}