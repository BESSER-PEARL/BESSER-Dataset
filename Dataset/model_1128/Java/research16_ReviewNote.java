





import java.util.List;
import java.util.ArrayList;

public class research16_ReviewNote extends Named {

    private String content;





    private research16_Paragraph research16_paragraph;


    public research16_ReviewNote(
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

    public research16_Paragraph getResearch16_paragraph() {
        return research16_paragraph;
    }

    public void setResearch16_paragraph(research16_Paragraph research16_paragraph) {
        this.research16_paragraph = research16_paragraph;
    }

}