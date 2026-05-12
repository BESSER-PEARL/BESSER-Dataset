





import java.util.List;
import java.util.ArrayList;

public class research32_ReviewNote extends Named {

    private String content;





    private research32_Paragraph research32_paragraph;


    public research32_ReviewNote(
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

    public research32_Paragraph getResearch32_paragraph() {
        return research32_paragraph;
    }

    public void setResearch32_paragraph(research32_Paragraph research32_paragraph) {
        this.research32_paragraph = research32_paragraph;
    }

}