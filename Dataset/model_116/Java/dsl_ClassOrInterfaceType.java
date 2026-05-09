





import java.util.List;
import java.util.ArrayList;

public class dsl_ClassOrInterfaceType  {

    private String ids;





    private dsl_ImplementsList dsl_implementslist;




    private dsl_ExtendsList dsl_extendslist;




    private dsl_ExtendsList dsl_extendslist;


    public dsl_ClassOrInterfaceType(
        String ids    ) {
        this.ids = ids;
    }


    public String getIds() {
        return ids;
    }

    public void setIds(String ids) {
        this.ids = ids;
    }

    public dsl_ImplementsList getDsl_implementslist() {
        return dsl_implementslist;
    }

    public void setDsl_implementslist(dsl_ImplementsList dsl_implementslist) {
        this.dsl_implementslist = dsl_implementslist;
    }
    public dsl_ExtendsList getDsl_extendslist() {
        return dsl_extendslist;
    }

    public void setDsl_extendslist(dsl_ExtendsList dsl_extendslist) {
        this.dsl_extendslist = dsl_extendslist;
    }
    public dsl_ExtendsList getDsl_extendslist() {
        return dsl_extendslist;
    }

    public void setDsl_extendslist(dsl_ExtendsList dsl_extendslist) {
        this.dsl_extendslist = dsl_extendslist;
    }

}