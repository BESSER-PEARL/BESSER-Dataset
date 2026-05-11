





import java.util.List;
import java.util.ArrayList;

public class modeldraw_Enumerator  {

    private String value;





    private modeldraw_NodeEnumerator modeldraw_nodeenumerator;


    public modeldraw_Enumerator(
        String value    ) {
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public modeldraw_NodeEnumerator getModeldraw_nodeenumerator() {
        return modeldraw_nodeenumerator;
    }

    public void setModeldraw_nodeenumerator(modeldraw_NodeEnumerator modeldraw_nodeenumerator) {
        this.modeldraw_nodeenumerator = modeldraw_nodeenumerator;
    }

}