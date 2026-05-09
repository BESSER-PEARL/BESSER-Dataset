





import java.util.List;
import java.util.ArrayList;

public class gedcoml_Note  {

    private String content;





    private gedcoml_BekanntePerson gedcoml_bekannteperson;


    public gedcoml_Note(
        String content    ) {
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public gedcoml_BekanntePerson getGedcoml_bekannteperson() {
        return gedcoml_bekannteperson;
    }

    public void setGedcoml_bekannteperson(gedcoml_BekanntePerson gedcoml_bekannteperson) {
        this.gedcoml_bekannteperson = gedcoml_bekannteperson;
    }

}