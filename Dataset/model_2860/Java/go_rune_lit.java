





import java.util.List;
import java.util.ArrayList;

public class go_rune_lit  {

    private String byte_value;
    private String unicode_value;





    private go_BasicLit go_basiclit;


    public go_rune_lit(
        String byte_value,        String unicode_value    ) {
        this.byte_value = byte_value;
        this.unicode_value = unicode_value;
    }


    public String getByte_value() {
        return byte_value;
    }

    public void setByte_value(String byte_value) {
        this.byte_value = byte_value;
    }
    public String getUnicode_value() {
        return unicode_value;
    }

    public void setUnicode_value(String unicode_value) {
        this.unicode_value = unicode_value;
    }

    public go_BasicLit getGo_basiclit() {
        return go_basiclit;
    }

    public void setGo_basiclit(go_BasicLit go_basiclit) {
        this.go_basiclit = go_basiclit;
    }

}