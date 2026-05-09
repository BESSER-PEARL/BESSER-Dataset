





import java.util.List;
import java.util.ArrayList;

public class tp4_ReviewNote extends Named {

    private String content;





    private tp4_Paragraph tp4_paragraph;


    public tp4_ReviewNote(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }

    public tp4_Paragraph getTp4_paragraph() {
        return tp4_paragraph;
    }

    public void setTp4_paragraph(tp4_Paragraph tp4_paragraph) {
        this.tp4_paragraph = tp4_paragraph;
    }

}