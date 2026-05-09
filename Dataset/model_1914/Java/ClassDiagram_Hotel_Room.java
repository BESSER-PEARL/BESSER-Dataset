





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Hotel_Room  {

    private int roomNumber;
    private boolean cleaningStatus;
    private boolean maintenceStatus;





    private ClassDiagram_Company_Hotel classdiagram_company_hotel;


    public ClassDiagram_Hotel_Room(
        int roomNumber,        boolean cleaningStatus,        boolean maintenceStatus    ) {
        this.roomNumber = roomNumber;
        this.cleaningStatus = cleaningStatus;
        this.maintenceStatus = maintenceStatus;
    }


    public int getRoomnumber() {
        return roomNumber;
    }

    public void setRoomnumber(int roomNumber) {
        this.roomNumber = roomNumber;
    }
    public boolean getCleaningstatus() {
        return cleaningStatus;
    }

    public void setCleaningstatus(boolean cleaningStatus) {
        this.cleaningStatus = cleaningStatus;
    }
    public boolean getMaintencestatus() {
        return maintenceStatus;
    }

    public void setMaintencestatus(boolean maintenceStatus) {
        this.maintenceStatus = maintenceStatus;
    }

    public ClassDiagram_Company_Hotel getClassdiagram_company_hotel() {
        return classdiagram_company_hotel;
    }

    public void setClassdiagram_company_hotel(ClassDiagram_Company_Hotel classdiagram_company_hotel) {
        this.classdiagram_company_hotel = classdiagram_company_hotel;
    }

}