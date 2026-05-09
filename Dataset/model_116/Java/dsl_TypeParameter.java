





import java.util.List;
import java.util.ArrayList;

public class dsl_TypeParameter  {

    private String id;





    private dsl_TypeParameters dsl_typeparameters;


    public dsl_TypeParameter(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public dsl_TypeParameters getDsl_typeparameters() {
        return dsl_typeparameters;
    }

    public void setDsl_typeparameters(dsl_TypeParameters dsl_typeparameters) {
        this.dsl_typeparameters = dsl_typeparameters;
    }

}