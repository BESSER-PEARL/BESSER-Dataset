





import java.util.List;
import java.util.ArrayList;

public class errors_CheckError extends Error {

    private String porcent;



    public errors_CheckError(
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