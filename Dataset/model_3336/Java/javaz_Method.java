





import java.util.List;
import java.util.ArrayList;

public class javaz_Method extends JavaElement {

    private boolean static;
    private boolean final;
    private String visibility;
    private boolean native;
    private boolean abstract;
    private boolean constructor;
    private boolean synchronized;





    private List<javaz_JavaParameter> javaz_javaparameters;




    private javaz_JavaClass javaz_javaclass;


    public javaz_Method(
        boolean static,        boolean final,        String visibility,        boolean native,        boolean abstract,        boolean constructor,        boolean synchronized    ) {
        super(
        );
        this.static = static;
        this.final = final;
        this.visibility = visibility;
        this.native = native;
        this.abstract = abstract;
        this.constructor = constructor;
        this.synchronized = synchronized;
        this.javaz_javaparameters = new ArrayList<>();
    }

    public javaz_Method(
        boolean static,        boolean final,        String visibility,        boolean native,        boolean abstract,        boolean constructor,        boolean synchronized        ArrayList<javaz_JavaParameter> javaz_javaparameters    ) {
        this.static = static;
        this.final = final;
        this.visibility = visibility;
        this.native = native;
        this.abstract = abstract;
        this.constructor = constructor;
        this.synchronized = synchronized;
        this.javaz_javaparameters = javaz_javaparameters;
    }

    public boolean getStatic() {
        return static;
    }

    public void setStatic(boolean static) {
        this.static = static;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
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
    public boolean getConstructor() {
        return constructor;
    }

    public void setConstructor(boolean constructor) {
        this.constructor = constructor;
    }
    public boolean getSynchronized() {
        return synchronized;
    }

    public void setSynchronized(boolean synchronized) {
        this.synchronized = synchronized;
    }

    public List<javaz_JavaParameter> getJavaz_javaparameters() {
        return javaz_javaparameters;
    }

    public void addJavaz_javaparameter(Javaz_javaparameter javaz_javaparameter) {
        this.javaz_javaparameters.add(javaz_javaparameter);
    }
    public javaz_JavaClass getJavaz_javaclass() {
        return javaz_javaclass;
    }

    public void setJavaz_javaclass(javaz_JavaClass javaz_javaclass) {
        this.javaz_javaclass = javaz_javaclass;
    }

}