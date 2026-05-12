





import java.util.List;
import java.util.ArrayList;

public class HotelBusiness  {






    private List<Hotel> hotels;


    public HotelBusiness(
    ) {
        this.hotels = new ArrayList<>();
    }

    public HotelBusiness(
        ArrayList<Hotel> hotels    ) {
        this.hotels = hotels;
    }


    public List<Hotel> getHotels() {
        return hotels;
    }

    public void addHotel(Hotel hotel) {
        this.hotels.add(hotel);
    }

}