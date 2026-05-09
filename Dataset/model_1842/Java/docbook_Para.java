





import java.util.List;
import java.util.ArrayList;

public class docbook_Para  {

    private String content;





    private docbook_Section docbook_section;


    public docbook_Para(
        String content    ) {
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public docbook_Section getDocbook_section() {
        return docbook_section;
    }

    public void setDocbook_section(docbook_Section docbook_section) {
        this.docbook_section = docbook_section;
    }

}