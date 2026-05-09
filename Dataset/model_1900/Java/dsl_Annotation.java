





import java.util.List;
import java.util.ArrayList;

public class dsl_Annotation extends Eclass {

    private String propertie;





    private dsl_AbstractClass dsl_abstractclass;




    private dsl_Library dsl_library;


    public dsl_Annotation(
        String propertie    ) {
        super(
        );
        this.propertie = propertie;
    }


    public String getPropertie() {
        return propertie;
    }

    public void setPropertie(String propertie) {
        this.propertie = propertie;
    }

    public dsl_AbstractClass getDsl_abstractclass() {
        return dsl_abstractclass;
    }

    public void setDsl_abstractclass(dsl_AbstractClass dsl_abstractclass) {
        this.dsl_abstractclass = dsl_abstractclass;
    }
    public dsl_Library getDsl_library() {
        return dsl_library;
    }

    public void setDsl_library(dsl_Library dsl_library) {
        this.dsl_library = dsl_library;
    }

}