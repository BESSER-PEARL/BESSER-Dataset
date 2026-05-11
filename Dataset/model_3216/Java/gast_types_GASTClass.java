





import java.util.List;
import java.util.ArrayList;

public class gast_types_GASTClass extends types_GASTType, types_Member {

    private boolean inner;
    private int linesOfComments;
    private boolean interface;
    private boolean local;
    private boolean anonymous;
    private boolean primitive;





    private Package package;


    public gast_types_GASTClass(
        boolean inner,        int linesOfComments,        boolean interface,        boolean local,        boolean anonymous,        boolean primitive    ) {
        super(
        );
        this.inner = inner;
        this.linesOfComments = linesOfComments;
        this.interface = interface;
        this.local = local;
        this.anonymous = anonymous;
        this.primitive = primitive;
    }


    public boolean getInner() {
        return inner;
    }

    public void setInner(boolean inner) {
        this.inner = inner;
    }
    public int getLinesofcomments() {
        return linesOfComments;
    }

    public void setLinesofcomments(int linesOfComments) {
        this.linesOfComments = linesOfComments;
    }
    public boolean getInterface() {
        return interface;
    }

    public void setInterface(boolean interface) {
        this.interface = interface;
    }
    public boolean getLocal() {
        return local;
    }

    public void setLocal(boolean local) {
        this.local = local;
    }
    public boolean getAnonymous() {
        return anonymous;
    }

    public void setAnonymous(boolean anonymous) {
        this.anonymous = anonymous;
    }
    public boolean getPrimitive() {
        return primitive;
    }

    public void setPrimitive(boolean primitive) {
        this.primitive = primitive;
    }

    public Package getPackage() {
        return package;
    }

    public void setPackage(Package package) {
        this.package = package;
    }

}