





import java.util.List;
import java.util.ArrayList;

public class dsl_MemberSelector  {

    private String id;





    private dsl_TypeArguments dsl_typearguments;




    private dsl_PrimarySuffix dsl_primarysuffix;


    public dsl_MemberSelector(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_TypeArguments getDsl_typearguments() {
        return dsl_typearguments;
    }

    public void setDsl_typearguments(dsl_TypeArguments dsl_typearguments) {
        this.dsl_typearguments = dsl_typearguments;
    }
    public dsl_PrimarySuffix getDsl_primarysuffix() {
        return dsl_primarysuffix;
    }

    public void setDsl_primarysuffix(dsl_PrimarySuffix dsl_primarysuffix) {
        this.dsl_primarysuffix = dsl_primarysuffix;
    }

}