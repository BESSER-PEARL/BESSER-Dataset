





import java.util.List;
import java.util.ArrayList;

public class shadowrun_Beschreibbar  {

    private String image;
    private String beschreibung;
    private String name;



    public shadowrun_Beschreibbar(
        String image,        String beschreibung,        String name    ) {
        this.image = image;
        this.beschreibung = beschreibung;
        this.name = name;
    }


    public String getImage() {
        return image;
    }

    public void setImage(String image) {
        this.image = image;
    }
    public String getBeschreibung() {
        return beschreibung;
    }

    public void setBeschreibung(String beschreibung) {
        this.beschreibung = beschreibung;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}