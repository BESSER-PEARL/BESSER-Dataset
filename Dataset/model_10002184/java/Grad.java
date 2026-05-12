





import java.util.List;
import java.util.ArrayList;

public class Grad  {

    private String NazivGrada;
    private int DrzavaID;
    private int GradID;





    private List<Hotel> hotels;


    public Grad(
        String NazivGrada,        int DrzavaID,        int GradID    ) {
        this.NazivGrada = NazivGrada;
        this.DrzavaID = DrzavaID;
        this.GradID = GradID;
        this.hotels = new ArrayList<>();
    }

    public Grad(
        String NazivGrada,        int DrzavaID,        int GradID        ArrayList<Hotel> hotels    ) {
        this.NazivGrada = NazivGrada;
        this.DrzavaID = DrzavaID;
        this.GradID = GradID;
        this.hotels = hotels;
    }

    public String getNazivgrada() {
        return NazivGrada;
    }

    public void setNazivgrada(String NazivGrada) {
        this.NazivGrada = NazivGrada;
    }
    public int getDrzavaid() {
        return DrzavaID;
    }

    public void setDrzavaid(int DrzavaID) {
        this.DrzavaID = DrzavaID;
    }
    public int getGradid() {
        return GradID;
    }

    public void setGradid(int GradID) {
        this.GradID = GradID;
    }

    public List<Hotel> getHotels() {
        return hotels;
    }

    public void addHotel(Hotel hotel) {
        this.hotels.add(hotel);
    }

}