




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Room_RoomKey  {

    private LocalDate expirationDate;





    private ClassDiagram_Hotel_Room classdiagram_hotel_room;


    public ClassDiagram_Room_RoomKey(
        LocalDate expirationDate    ) {
        this.expirationDate = expirationDate;
    }


    public LocalDate getExpirationdate() {
        return expirationDate;
    }

    public void setExpirationdate(LocalDate expirationDate) {
        this.expirationDate = expirationDate;
    }

    public ClassDiagram_Hotel_Room getClassdiagram_hotel_room() {
        return classdiagram_hotel_room;
    }

    public void setClassdiagram_hotel_room(ClassDiagram_Hotel_Room classdiagram_hotel_room) {
        this.classdiagram_hotel_room = classdiagram_hotel_room;
    }

}