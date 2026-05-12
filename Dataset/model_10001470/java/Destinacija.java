





import java.util.List;
import java.util.ArrayList;

public class Destinacija  {

    private String Hotel;
    private String Drzava;
    private String Grad;
    private int DestinacijaID;





    private Aranzman aranzman;


    public Destinacija(
        String Hotel,        String Drzava,        String Grad,        int DestinacijaID    ) {
        this.Hotel = Hotel;
        this.Drzava = Drzava;
        this.Grad = Grad;
        this.DestinacijaID = DestinacijaID;
    }


    public String getHotel() {
        return Hotel;
    }

    public void setHotel(String Hotel) {
        this.Hotel = Hotel;
    }
    public String getDrzava() {
        return Drzava;
    }

    public void setDrzava(String Drzava) {
        this.Drzava = Drzava;
    }
    public String getGrad() {
        return Grad;
    }

    public void setGrad(String Grad) {
        this.Grad = Grad;
    }
    public int getDestinacijaid() {
        return DestinacijaID;
    }

    public void setDestinacijaid(int DestinacijaID) {
        this.DestinacijaID = DestinacijaID;
    }

    public Aranzman getAranzman() {
        return aranzman;
    }

    public void setAranzman(Aranzman aranzman) {
        this.aranzman = aranzman;
    }

}