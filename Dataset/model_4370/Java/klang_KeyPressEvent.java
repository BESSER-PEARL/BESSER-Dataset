





import java.util.List;
import java.util.ArrayList;

public class klang_KeyPressEvent extends GlobalEvent {

    private String key;



    public klang_KeyPressEvent(
        String key    ) {
        super(
        );
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }


}