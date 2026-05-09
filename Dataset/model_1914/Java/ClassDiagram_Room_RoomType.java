





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Room_RoomType  {

    private String name;
    private float area;
    private float price;
    private int maxNumberOfGuests;





    private ClassDiagram_Company_Hotel classdiagram_company_hotel;




    private ClassDiagram_Hotel_Room classdiagram_hotel_room;


    public ClassDiagram_Room_RoomType(
        String name,        float area,        float price,        int maxNumberOfGuests    ) {
        this.name = name;
        this.area = area;
        this.price = price;
        this.maxNumberOfGuests = maxNumberOfGuests;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public int getMaxnumberofguests() {
        return maxNumberOfGuests;
    }

    public void setMaxnumberofguests(int maxNumberOfGuests) {
        this.maxNumberOfGuests = maxNumberOfGuests;
    }

    public ClassDiagram_Company_Hotel getClassdiagram_company_hotel() {
        return classdiagram_company_hotel;
    }

    public void setClassdiagram_company_hotel(ClassDiagram_Company_Hotel classdiagram_company_hotel) {
        this.classdiagram_company_hotel = classdiagram_company_hotel;
    }
    public ClassDiagram_Hotel_Room getClassdiagram_hotel_room() {
        return classdiagram_hotel_room;
    }

    public void setClassdiagram_hotel_room(ClassDiagram_Hotel_Room classdiagram_hotel_room) {
        this.classdiagram_hotel_room = classdiagram_hotel_room;
    }

}