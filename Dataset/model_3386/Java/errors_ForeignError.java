





import java.util.List;
import java.util.ArrayList;

public class errors_ForeignError extends Error {

    private int porcent;



    public errors_ForeignError(
        int porcent    ) {
        super(
        );
        this.porcent = porcent;
    }


    public int getPorcent() {
        return porcent;
    }

    public void setPorcent(int porcent) {
        this.porcent = porcent;
    }


}