





import java.util.List;
import java.util.ArrayList;

public class room_Attribute  {

    private int size;
    private String name;
    private String defaultValueLiteral;





    private room_RefableType room_refabletype;




    private room_DataClass room_dataclass;


    public room_Attribute(
        int size,        String name,        String defaultValueLiteral    ) {
        this.size = size;
        this.name = name;
        this.defaultValueLiteral = defaultValueLiteral;
    }


    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }

    public room_RefableType getRoom_refabletype() {
        return room_refabletype;
    }

    public void setRoom_refabletype(room_RefableType room_refabletype) {
        this.room_refabletype = room_refabletype;
    }
    public room_DataClass getRoom_dataclass() {
        return room_dataclass;
    }

    public void setRoom_dataclass(room_DataClass room_dataclass) {
        this.room_dataclass = room_dataclass;
    }

}