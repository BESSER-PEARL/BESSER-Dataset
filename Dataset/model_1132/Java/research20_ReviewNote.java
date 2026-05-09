





import java.util.List;
import java.util.ArrayList;

public class research20_ReviewNote extends Named {

    private String content;





    private research20_Paragraph research20_paragraph;


    public research20_ReviewNote(
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

    public research20_Paragraph getResearch20_paragraph() {
        return research20_paragraph;
    }

    public void setResearch20_paragraph(research20_Paragraph research20_paragraph) {
        this.research20_paragraph = research20_paragraph;
    }

}