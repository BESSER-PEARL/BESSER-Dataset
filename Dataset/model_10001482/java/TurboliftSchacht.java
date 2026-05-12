





import java.util.List;
import java.util.ArrayList;

public class TurboliftSchacht  {

    private boolean vertikal;





    private Steuerung steuerung;




    private TurboliftSystem turboliftsystem;


    public TurboliftSchacht(
        boolean vertikal    ) {
        this.vertikal = vertikal;
    }


    public boolean getVertikal() {
        return vertikal;
    }

    public void setVertikal(boolean vertikal) {
        this.vertikal = vertikal;
    }

    public Steuerung getSteuerung() {
        return steuerung;
    }

    public void setSteuerung(Steuerung steuerung) {
        this.steuerung = steuerung;
    }
    public TurboliftSystem getTurboliftsystem() {
        return turboliftsystem;
    }

    public void setTurboliftsystem(TurboliftSystem turboliftsystem) {
        this.turboliftsystem = turboliftsystem;
    }

}