





import java.util.List;
import java.util.ArrayList;

public class javaz_JavaClass extends JavaElement {

    private String kind;
    private boolean needToGenerate;
    private boolean public;
    private boolean final;
    private boolean rewritable;





    private javaz_JavaClass javaz_javaclass;




    private javaz_Javaz javaz_javaz;




    private javaz_JavaClass javaz_javaclass;




    private List<javaz_Method> javaz_methods;




    private javaz_JavaClass javaz_javaclass;


    public javaz_JavaClass(
        String kind,        boolean needToGenerate,        boolean public,        boolean final,        boolean rewritable    ) {
        super(
        );
        this.kind = kind;
        this.needToGenerate = needToGenerate;
        this.public = public;
        this.final = final;
        this.rewritable = rewritable;
        this.javaz_methods = new ArrayList<>();
    }

    public javaz_JavaClass(
        String kind,        boolean needToGenerate,        boolean public,        boolean final,        boolean rewritable        ArrayList<javaz_Method> javaz_methods    ) {
        this.kind = kind;
        this.needToGenerate = needToGenerate;
        this.public = public;
        this.final = final;
        this.rewritable = rewritable;
        this.javaz_methods = javaz_methods;
    }

    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }
    public boolean getNeedtogenerate() {
        return needToGenerate;
    }

    public void setNeedtogenerate(boolean needToGenerate) {
        this.needToGenerate = needToGenerate;
    }
    public boolean getPublic() {
        return public;
    }

    public void setPublic(boolean public) {
        this.public = public;
    }
    public boolean getFinal() {
        return final;
    }

    public void setFinal(boolean final) {
        this.final = final;
    }
    public boolean getRewritable() {
        return rewritable;
    }

    public void setRewritable(boolean rewritable) {
        this.rewritable = rewritable;
    }

    public javaz_JavaClass getJavaz_javaclass() {
        return javaz_javaclass;
    }

    public void setJavaz_javaclass(javaz_JavaClass javaz_javaclass) {
        this.javaz_javaclass = javaz_javaclass;
    }
    public javaz_Javaz getJavaz_javaz() {
        return javaz_javaz;
    }

    public void setJavaz_javaz(javaz_Javaz javaz_javaz) {
        this.javaz_javaz = javaz_javaz;
    }
    public javaz_JavaClass getJavaz_javaclass() {
        return javaz_javaclass;
    }

    public void setJavaz_javaclass(javaz_JavaClass javaz_javaclass) {
        this.javaz_javaclass = javaz_javaclass;
    }
    public List<javaz_Method> getJavaz_methods() {
        return javaz_methods;
    }

    public void addJavaz_method(Javaz_method javaz_method) {
        this.javaz_methods.add(javaz_method);
    }
    public javaz_JavaClass getJavaz_javaclass() {
        return javaz_javaclass;
    }

    public void setJavaz_javaclass(javaz_JavaClass javaz_javaclass) {
        this.javaz_javaclass = javaz_javaclass;
    }

}