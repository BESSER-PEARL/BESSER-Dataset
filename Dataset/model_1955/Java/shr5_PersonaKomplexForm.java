





import java.util.List;
import java.util.ArrayList;

public class shr5_PersonaKomplexForm extends Erlernbar {

    private int stufe;





    private shr5_Technomancer shr5_technomancer;




    private shr5_KomplexeForm shr5_komplexeform;


    public shr5_PersonaKomplexForm(
        int stufe    ) {
        super(
        );
        this.stufe = stufe;
    }


    public int getStufe() {
        return stufe;
    }

    public void setStufe(int stufe) {
        this.stufe = stufe;
    }

    public shr5_Technomancer getShr5_technomancer() {
        return shr5_technomancer;
    }

    public void setShr5_technomancer(shr5_Technomancer shr5_technomancer) {
        this.shr5_technomancer = shr5_technomancer;
    }
    public shr5_KomplexeForm getShr5_komplexeform() {
        return shr5_komplexeform;
    }

    public void setShr5_komplexeform(shr5_KomplexeForm shr5_komplexeform) {
        this.shr5_komplexeform = shr5_komplexeform;
    }

}