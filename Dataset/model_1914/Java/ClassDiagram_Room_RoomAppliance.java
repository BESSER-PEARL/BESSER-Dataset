





import java.util.List;
import java.util.ArrayList;

public class ClassDiagram_Room_RoomAppliance  {

    private String name;





    private ClassDiagram_RoomAppliance_ApplianceType classdiagram_roomappliance_appliancetype;


    public ClassDiagram_Room_RoomAppliance(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ClassDiagram_RoomAppliance_ApplianceType getClassdiagram_roomappliance_appliancetype() {
        return classdiagram_roomappliance_appliancetype;
    }

    public void setClassdiagram_roomappliance_appliancetype(ClassDiagram_RoomAppliance_ApplianceType classdiagram_roomappliance_appliancetype) {
        this.classdiagram_roomappliance_appliancetype = classdiagram_roomappliance_appliancetype;
    }

}