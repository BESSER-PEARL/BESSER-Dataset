





import java.util.List;
import java.util.ArrayList;

public class room_PrimitiveType extends DataType {

    private String targetName;
    private String defaultValueLiteral;
    private String castName;
    private String type;





    private room_RoomModel room_roommodel;


    public room_PrimitiveType(
        String targetName,        String defaultValueLiteral,        String castName,        String type    ) {
        super(
        );
        this.targetName = targetName;
        this.defaultValueLiteral = defaultValueLiteral;
        this.castName = castName;
        this.type = type;
    }


    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }
    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }
    public String getCastname() {
        return castName;
    }

    public void setCastname(String castName) {
        this.castName = castName;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public room_RoomModel getRoom_roommodel() {
        return room_roommodel;
    }

    public void setRoom_roommodel(room_RoomModel room_roommodel) {
        this.room_roommodel = room_roommodel;
    }

}