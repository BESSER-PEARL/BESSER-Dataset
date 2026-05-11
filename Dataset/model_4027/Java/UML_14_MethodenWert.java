





import java.util.List;
import java.util.ArrayList;

public class UML_14_MethodenWert extends Benanntes {

    private String art;
    private String standartWert;



    public UML_14_MethodenWert(
        String art,        String standartWert    ) {
        super(
        );
        this.art = art;
        this.standartWert = standartWert;
    }


    public String getArt() {
        return art;
    }

    public void setArt(String art) {
        this.art = art;
    }
    public String getStandartwert() {
        return standartWert;
    }

    public void setStandartwert(String standartWert) {
        this.standartWert = standartWert;
    }


}