





import java.util.List;
import java.util.ArrayList;

public class javaz_JavaPackageX extends JavaElement {

    private boolean needToGenerate;





    private javaz_Javaz javaz_javaz;




    private javaz_JavaClass javaz_javaclass;


    public javaz_JavaPackageX(
        boolean needToGenerate    ) {
        super(
        );
        this.needToGenerate = needToGenerate;
    }


    public boolean getNeedtogenerate() {
        return needToGenerate;
    }

    public void setNeedtogenerate(boolean needToGenerate) {
        this.needToGenerate = needToGenerate;
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

}