





import java.util.List;
import java.util.ArrayList;

public class room_KeyValue  {

    private String value;
    private String key;





    private room_Annotation room_annotation;


    public room_KeyValue(
        String value,        String key    ) {
        this.value = value;
        this.key = key;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public room_Annotation getRoom_annotation() {
        return room_annotation;
    }

    public void setRoom_annotation(room_Annotation room_annotation) {
        this.room_annotation = room_annotation;
    }

}