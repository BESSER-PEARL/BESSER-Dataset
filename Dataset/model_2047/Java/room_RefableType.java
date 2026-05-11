





import java.util.List;
import java.util.ArrayList;

public class room_RefableType  {

    private boolean ref;





    private room_VarDecl room_vardecl;




    private room_DataType room_datatype;




    private room_Operation room_operation;




    private room_Attribute room_attribute;


    public room_RefableType(
        boolean ref    ) {
        this.ref = ref;
    }


    public boolean getRef() {
        return ref;
    }

    public void setRef(boolean ref) {
        this.ref = ref;
    }

    public room_VarDecl getRoom_vardecl() {
        return room_vardecl;
    }

    public void setRoom_vardecl(room_VarDecl room_vardecl) {
        this.room_vardecl = room_vardecl;
    }
    public room_DataType getRoom_datatype() {
        return room_datatype;
    }

    public void setRoom_datatype(room_DataType room_datatype) {
        this.room_datatype = room_datatype;
    }
    public room_Operation getRoom_operation() {
        return room_operation;
    }

    public void setRoom_operation(room_Operation room_operation) {
        this.room_operation = room_operation;
    }
    public room_Attribute getRoom_attribute() {
        return room_attribute;
    }

    public void setRoom_attribute(room_Attribute room_attribute) {
        this.room_attribute = room_attribute;
    }

}