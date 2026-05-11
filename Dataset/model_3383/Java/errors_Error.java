





import java.util.List;
import java.util.ArrayList;

public class errors_Error  {

    private String apply;
    private String id;





    private errors_Errores errors_errores;


    public errors_Error(
        String apply,        String id    ) {
        this.apply = apply;
        this.id = id;
    }


    public String getApply() {
        return apply;
    }

    public void setApply(String apply) {
        this.apply = apply;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public errors_Errores getErrors_errores() {
        return errors_errores;
    }

    public void setErrors_errores(errors_Errores errors_errores) {
        this.errors_errores = errors_errores;
    }

}