





import java.util.List;
import java.util.ArrayList;

public class gedcoml_Married  {

    private String weddingDay;
    private String separationDay;



    public gedcoml_Married(
        String weddingDay,        String separationDay    ) {
        this.weddingDay = weddingDay;
        this.separationDay = separationDay;
    }


    public String getWeddingday() {
        return weddingDay;
    }

    public void setWeddingday(String weddingDay) {
        this.weddingDay = weddingDay;
    }
    public String getSeparationday() {
        return separationDay;
    }

    public void setSeparationday(String separationDay) {
        this.separationDay = separationDay;
    }


}