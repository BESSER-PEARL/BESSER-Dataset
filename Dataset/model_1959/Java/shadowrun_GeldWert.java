





import java.util.List;
import java.util.ArrayList;

public class shadowrun_GeldWert  {

    private String wert;
    private float strassenIndex;
    private String verfuegbarkeit;



    public shadowrun_GeldWert(
        String wert,        float strassenIndex,        String verfuegbarkeit    ) {
        this.wert = wert;
        this.strassenIndex = strassenIndex;
        this.verfuegbarkeit = verfuegbarkeit;
    }


    public String getWert() {
        return wert;
    }

    public void setWert(String wert) {
        this.wert = wert;
    }
    public float getStrassenindex() {
        return strassenIndex;
    }

    public void setStrassenindex(float strassenIndex) {
        this.strassenIndex = strassenIndex;
    }
    public String getVerfuegbarkeit() {
        return verfuegbarkeit;
    }

    public void setVerfuegbarkeit(String verfuegbarkeit) {
        this.verfuegbarkeit = verfuegbarkeit;
    }


}