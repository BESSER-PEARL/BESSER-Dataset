





import java.util.List;
import java.util.ArrayList;

public class errorstm_Action  {

    private String kind;





    private errorstm_AbstractState errorstm_abstractstate;


    public errorstm_Action(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public errorstm_AbstractState getErrorstm_abstractstate() {
        return errorstm_abstractstate;
    }

    public void setErrorstm_abstractstate(errorstm_AbstractState errorstm_abstractstate) {
        this.errorstm_abstractstate = errorstm_abstractstate;
    }

}