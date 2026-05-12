





import java.util.List;
import java.util.ArrayList;

public class HouseKeeping_Actor  {






    private Room_Cleaning_UseCase room_cleaning_usecase;


    public HouseKeeping_Actor(
    ) {
    }



    public Room_Cleaning_UseCase getRoom_cleaning_usecase() {
        return room_cleaning_usecase;
    }

    public void setRoom_cleaning_usecase(Room_Cleaning_UseCase room_cleaning_usecase) {
        this.room_cleaning_usecase = room_cleaning_usecase;
    }

}