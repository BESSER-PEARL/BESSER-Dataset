





import java.util.List;
import java.util.ArrayList;

public class DVE_model_Reference extends Expression {

    private String refName;



    public DVE_model_Reference(
        String refName    ) {
        super(
        );
        this.refName = refName;
    }


    public String getRefname() {
        return refName;
    }

    public void setRefname(String refName) {
        this.refName = refName;
    }


}