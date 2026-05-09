





import java.util.List;
import java.util.ArrayList;

public class newClasses_Manager extends RoomHandlerInterface, ServiceHandlerInterface, ManagerInterface {

    private String password;
    private String userName;





    private newClasses_RoomHandler newclasses_roomhandler;




    private newClasses_ServiceHandler newclasses_servicehandler;


    public newClasses_Manager(
        String password,        String userName    ) {
        super(
        );
        this.password = password;
        this.userName = userName;
    }


    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getUsername() {
        return userName;
    }

    public void setUsername(String userName) {
        this.userName = userName;
    }

    public newClasses_RoomHandler getNewclasses_roomhandler() {
        return newclasses_roomhandler;
    }

    public void setNewclasses_roomhandler(newClasses_RoomHandler newclasses_roomhandler) {
        this.newclasses_roomhandler = newclasses_roomhandler;
    }
    public newClasses_ServiceHandler getNewclasses_servicehandler() {
        return newclasses_servicehandler;
    }

    public void setNewclasses_servicehandler(newClasses_ServiceHandler newclasses_servicehandler) {
        this.newclasses_servicehandler = newclasses_servicehandler;
    }

}