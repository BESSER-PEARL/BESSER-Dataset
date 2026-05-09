





import java.util.List;
import java.util.ArrayList;

public class shr5_Beschreibbar  {

    private String beschreibung;
    private String image;
    private String name;



    public shr5_Beschreibbar(
        String beschreibung,        String image,        String name    ) {
        this.beschreibung = beschreibung;
        this.image = image;
        this.name = name;
    }


    public String getBeschreibung() {
        return beschreibung;
    }

    public void setBeschreibung(String beschreibung) {
        this.beschreibung = beschreibung;
    }
    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}