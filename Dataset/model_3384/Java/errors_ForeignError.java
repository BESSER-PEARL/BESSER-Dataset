





import java.util.List;
import java.util.ArrayList;

public class errors_ForeignError extends Error {

    private String nameFk;
    private String porcent;



    public errors_ForeignError(
        String nameFk,        String porcent    ) {
        super(
        );
        this.nameFk = nameFk;
        this.porcent = porcent;
    }


    public String getNamefk() {
        return nameFk;
    }

    public void setNamefk(String nameFk) {
        this.nameFk = nameFk;
    }
    public String getPorcent() {
        return porcent;
    }

    public void setPorcent(String porcent) {
        this.porcent = porcent;
    }


}