





import java.util.List;
import java.util.ArrayList;

public class javaz_Method extends JavaElement {

    private boolean static;
    private boolean synchronized;
    private boolean final;
    private boolean constructor;
    private String visibility;
    private boolean native;
    private boolean abstract;



    public javaz_Method(
        boolean static,        boolean synchronized,        boolean final,        boolean constructor,        String visibility,        boolean native,        boolean abstract    ) {
        super(
        );
        this.static = static;
        this.synchronized = synchronized;
        this.final = final;
        this.constructor = constructor;
        this.visibility = visibility;
        this.native = native;
        this.abstract = abstract;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getConstructor() {
        return constructor;
    }

    public void setConstructor(boolean constructor) {
        this.constructor = constructor;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getNative() {
        return native;
    }

    public void setNative(boolean native) {
        this.native = native;
    }
    public boolean getAbstract() {
        return abstract;
    }

    public void setAbstract(boolean abstract) {
        this.abstract = abstract;
    }


}