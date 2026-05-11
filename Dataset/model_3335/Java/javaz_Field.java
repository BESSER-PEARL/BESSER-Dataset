





import java.util.List;
import java.util.ArrayList;

public class javaz_Field extends JavaElement {

    private boolean static;
    private boolean volatile;
    private boolean transient;
    private String type;
    private String visibility;
    private boolean final;





    private javaz_JavaClass javaz_javaclass;


    public javaz_Field(
        boolean static,        boolean volatile,        boolean transient,        String type,        String visibility,        boolean final    ) {
        super(
        );
        this.static = static;
        this.volatile = volatile;
        this.transient = transient;
        this.type = type;
        this.visibility = visibility;
        this.final = final;
    }


    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getVolatile() {
        return volatile;
    }

    public void setVolatile(boolean volatile) {
        this.volatile = volatile;
    }
    public boolean getTransient() {
        return transient;
    }

    public void setTransient(boolean transient) {
        this.transient = transient;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getVisibility() {
        return visibility;
    }

    public void setVisibility(String visibility) {
        this.visibility = visibility;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }

    public javaz_JavaClass getJavaz_javaclass() {
        return javaz_javaclass;
    }

    public void setJavaz_javaclass(javaz_JavaClass javaz_javaclass) {
        this.javaz_javaclass = javaz_javaclass;
    }

}