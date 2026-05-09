





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Room_RoomType  {

    private int maxNumberOfGuests;
    private float area;
    private float price;





    private ClassDiagram_Hotel_Room classdiagram_hotel_room;


    public ClassDiagram_Room_RoomType(
        int maxNumberOfGuests,        float area,        float price    ) {
        this.maxNumberOfGuests = maxNumberOfGuests;
        this.area = area;
        this.price = price;
    }


    public int getMaxnumberofguests() {
        return maxNumberOfGuests;
    }

    public void setMaxnumberofguests(int maxNumberOfGuests) {
        this.maxNumberOfGuests = maxNumberOfGuests;
    }
    public float getArea() {
        return area;
    }

    public void setArea(float area) {
        this.area = area;
    }
    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }

    public ClassDiagram_Hotel_Room getClassdiagram_hotel_room() {
        return classdiagram_hotel_room;
    }

    public void setClassdiagram_hotel_room(ClassDiagram_Hotel_Room classdiagram_hotel_room) {
        this.classdiagram_hotel_room = classdiagram_hotel_room;
    }

}