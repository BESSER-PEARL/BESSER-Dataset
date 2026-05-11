





import java.util.List;
import java.util.ArrayList;

public class room_VarDecl  {

    private String name;





    private room_Operation room_operation;


    public room_VarDecl(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public room_Operation getRoom_operation() {
        return room_operation;
    }

    public void setRoom_operation(room_Operation room_operation) {
        this.room_operation = room_operation;
    }

}