





import java.util.List;
import java.util.ArrayList;

public class Freemind_CloudType  {

    private String Color;





    private Freemind_DocumentRoot freemind_documentroot;


    public Freemind_CloudType(
        String Color    ) {
        this.Color = Color;
    }


    public String getColor() {
        return Color;
    }

    public void setColor(String Color) {
        this.Color = Color;
    }

    public Freemind_DocumentRoot getFreemind_documentroot() {
        return freemind_documentroot;
    }

    public void setFreemind_documentroot(Freemind_DocumentRoot freemind_documentroot) {
        this.freemind_documentroot = freemind_documentroot;
    }

}