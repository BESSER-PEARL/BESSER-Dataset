





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Facility_FacilityType  {

    private String name;





    private ClassDiagram_Hotel_Facility classdiagram_hotel_facility;


    public ClassDiagram_Facility_FacilityType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassDiagram_Hotel_Facility getClassdiagram_hotel_facility() {
        return classdiagram_hotel_facility;
    }

    public void setClassdiagram_hotel_facility(ClassDiagram_Hotel_Facility classdiagram_hotel_facility) {
        this.classdiagram_hotel_facility = classdiagram_hotel_facility;
    }

}