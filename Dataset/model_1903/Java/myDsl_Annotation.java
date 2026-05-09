





import java.util.List;
import java.util.ArrayList;

public class myDsl_Annotation extends Eclass {

    private String propertie;





    private myDsl_Library mydsl_library;




    private myDsl_GenericClass mydsl_genericclass;




    private myDsl_AbstractClass mydsl_abstractclass;


    public myDsl_Annotation(
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

    public myDsl_Library getMydsl_library() {
        return mydsl_library;
    }

    public void setMydsl_library(myDsl_Library mydsl_library) {
        this.mydsl_library = mydsl_library;
    }
    public myDsl_GenericClass getMydsl_genericclass() {
        return mydsl_genericclass;
    }

    public void setMydsl_genericclass(myDsl_GenericClass mydsl_genericclass) {
        this.mydsl_genericclass = mydsl_genericclass;
    }
    public myDsl_AbstractClass getMydsl_abstractclass() {
        return mydsl_abstractclass;
    }

    public void setMydsl_abstractclass(myDsl_AbstractClass mydsl_abstractclass) {
        this.mydsl_abstractclass = mydsl_abstractclass;
    }

}