





import java.util.List;
import java.util.ArrayList;

public class research23_ReviewNote extends Named {

    private String content;





    private research23_Paragraph research23_paragraph;


    public research23_ReviewNote(
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

    public research23_Paragraph getResearch23_paragraph() {
        return research23_paragraph;
    }

    public void setResearch23_paragraph(research23_Paragraph research23_paragraph) {
        this.research23_paragraph = research23_paragraph;
    }

}