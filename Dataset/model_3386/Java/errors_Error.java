





import java.util.List;
import java.util.ArrayList;

public class errors_Error  {

    private boolean apply;
    private int id;





    private errors_Errores errors_errores;


    public errors_Error(
        boolean apply,        int id    ) {
        this.apply = apply;
        this.id = id;
    }


    public boolean getApply() {
        return apply;
    }

    public void setApply(boolean apply) {
        this.apply = apply;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public errors_Errores getErrors_errores() {
        return errors_errores;
    }

    public void setErrors_errores(errors_Errores errors_errores) {
        this.errors_errores = errors_errores;
    }

}