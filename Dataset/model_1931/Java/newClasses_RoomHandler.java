





import java.util.List;
import java.util.ArrayList;

public class newClasses_RoomHandler extends RoomProvider, RoomHandlerInterface, GuestInterface {






    private newClasses_Database newclasses_database;


    public newClasses_RoomHandler(
    ) {
        super(
        );
    }



    public newClasses_Database getNewclasses_database() {
        return newclasses_database;
    }

    public void setNewclasses_database(newClasses_Database newclasses_database) {
        this.newclasses_database = newclasses_database;
    }

}