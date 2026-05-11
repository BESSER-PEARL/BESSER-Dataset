





import java.util.List;
import java.util.ArrayList;

public class room_PrimitiveType extends DataType {

    private String defaultValueLiteral;
    private String type;
    private String targetName;
    private String castName;





    private room_RoomModel room_roommodel;


    public room_PrimitiveType(
        String defaultValueLiteral,        String type,        String targetName,        String castName    ) {
        super(
        );
        this.defaultValueLiteral = defaultValueLiteral;
        this.type = type;
        this.targetName = targetName;
        this.castName = castName;
    }


    public String getDefaultvalueliteral() {
        return defaultValueLiteral;
    }

    public void setDefaultvalueliteral(String defaultValueLiteral) {
        this.defaultValueLiteral = defaultValueLiteral;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }
    public String getCastname() {
        return castName;
    }

    public void setCastname(String castName) {
        this.castName = castName;
    }

    public room_RoomModel getRoom_roommodel() {
        return room_roommodel;
    }

    public void setRoom_roommodel(room_RoomModel room_roommodel) {
        this.room_roommodel = room_roommodel;
    }

}