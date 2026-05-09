





import java.util.List;
import java.util.ArrayList;

public class shr5_Fakeable extends Vertrag {

    private int stufe;
    private boolean gefaelscht;



    public shr5_Fakeable(
        int stufe,        boolean gefaelscht    ) {
        super(
        );
        this.stufe = stufe;
        this.gefaelscht = gefaelscht;
    }


    public int getStufe() {
        return stufe;
    }

    public void setStufe(int stufe) {
        this.stufe = stufe;
    }
    public boolean getGefaelscht() {
        return gefaelscht;
    }

    public void setGefaelscht(boolean gefaelscht) {
        this.gefaelscht = gefaelscht;
    }


}