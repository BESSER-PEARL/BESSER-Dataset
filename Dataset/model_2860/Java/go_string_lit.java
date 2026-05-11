





import java.util.List;
import java.util.ArrayList;

public class go_string_lit  {

    private String interpreted_string_lit;
    private String raw_string_lit;





    private go_Tag go_tag;


    public go_string_lit(
        String interpreted_string_lit,        String raw_string_lit    ) {
        this.interpreted_string_lit = interpreted_string_lit;
        this.raw_string_lit = raw_string_lit;
    }


    public String getInterpreted_string_lit() {
        return interpreted_string_lit;
    }

    public void setInterpreted_string_lit(String interpreted_string_lit) {
        this.interpreted_string_lit = interpreted_string_lit;
    }
    public String getRaw_string_lit() {
        return raw_string_lit;
    }

    public void setRaw_string_lit(String raw_string_lit) {
        this.raw_string_lit = raw_string_lit;
    }

    public go_Tag getGo_tag() {
        return go_tag;
    }

    public void setGo_tag(go_Tag go_tag) {
        this.go_tag = go_tag;
    }

}