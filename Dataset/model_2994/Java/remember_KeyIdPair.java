





import java.util.List;
import java.util.ArrayList;

public class remember_KeyIdPair  {

    private String key;
    private String id;





    private remember_KeyManager remember_keymanager;


    public remember_KeyIdPair(
        String key,        String id    ) {
        this.key = key;
        this.id = id;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public remember_KeyManager getRemember_keymanager() {
        return remember_keymanager;
    }

    public void setRemember_keymanager(remember_KeyManager remember_keymanager) {
        this.remember_keymanager = remember_keymanager;
    }

}