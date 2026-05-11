





import java.util.List;
import java.util.ArrayList;

public class imp_StringToValueMap  {

    private String key;





    private imp_Store imp_store;


    public imp_StringToValueMap(
        String key    ) {
        this.key = key;
    }


    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public imp_Store getImp_store() {
        return imp_store;
    }

    public void setImp_store(imp_Store imp_store) {
        this.imp_store = imp_store;
    }

}