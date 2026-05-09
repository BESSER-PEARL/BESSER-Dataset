





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Facility_FacilityType  {

    private String kind;





    private ClassDiagram_Hotel_Facility classdiagram_hotel_facility;


    public ClassDiagram_Facility_FacilityType(
        String kind    ) {
        this.kind = kind;
    }


    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public ClassDiagram_Hotel_Facility getClassdiagram_hotel_facility() {
        return classdiagram_hotel_facility;
    }

    public void setClassdiagram_hotel_facility(ClassDiagram_Hotel_Facility classdiagram_hotel_facility) {
        this.classdiagram_hotel_facility = classdiagram_hotel_facility;
    }

}