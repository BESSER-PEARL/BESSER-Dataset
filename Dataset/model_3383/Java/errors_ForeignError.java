





import java.util.List;
import java.util.ArrayList;

public class errors_ForeignError extends Error {

    private String porcent;



    public errors_ForeignError(
        String porcent    ) {
        super(
        );
        this.porcent = porcent;
    }


    public String getPorcent() {
        return porcent;
    }

    public void setPorcent(String porcent) {
        this.porcent = porcent;
    }


}