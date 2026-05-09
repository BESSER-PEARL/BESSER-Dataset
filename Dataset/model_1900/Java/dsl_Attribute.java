





import java.util.List;
import java.util.ArrayList;

public class dsl_Attribute  {

    private String name;





    private dsl_NativeClass dsl_nativeclass;




    private dsl_GenericClass dsl_genericclass;




    private dsl_AbstractClass dsl_abstractclass;


    public dsl_Attribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_NativeClass getDsl_nativeclass() {
        return dsl_nativeclass;
    }

    public void setDsl_nativeclass(dsl_NativeClass dsl_nativeclass) {
        this.dsl_nativeclass = dsl_nativeclass;
    }
    public dsl_GenericClass getDsl_genericclass() {
        return dsl_genericclass;
    }

    public void setDsl_genericclass(dsl_GenericClass dsl_genericclass) {
        this.dsl_genericclass = dsl_genericclass;
    }
    public dsl_AbstractClass getDsl_abstractclass() {
        return dsl_abstractclass;
    }

    public void setDsl_abstractclass(dsl_AbstractClass dsl_abstractclass) {
        this.dsl_abstractclass = dsl_abstractclass;
    }

}