





import java.util.List;
import java.util.ArrayList;

public class Implementation_RoomComponent_Bedroom extends RoomComponent_Room {

    private String bedCount;





    private Implementation_RoomComponent_RoomHandler implementation_roomcomponent_roomhandler;


    public Implementation_RoomComponent_Bedroom(
        String bedCount    ) {
        super(
        );
        this.bedCount = bedCount;
    }


    public String getBedcount() {
        return bedCount;
    }

    public void setBedcount(String bedCount) {
        this.bedCount = bedCount;
    }

    public Implementation_RoomComponent_RoomHandler getImplementation_roomcomponent_roomhandler() {
        return implementation_roomcomponent_roomhandler;
    }

    public void setImplementation_roomcomponent_roomhandler(Implementation_RoomComponent_RoomHandler implementation_roomcomponent_roomhandler) {
        this.implementation_roomcomponent_roomhandler = implementation_roomcomponent_roomhandler;
    }

}