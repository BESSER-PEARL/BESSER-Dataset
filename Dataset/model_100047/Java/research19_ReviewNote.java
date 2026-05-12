





import java.util.List;
import java.util.ArrayList;

public class research19_ReviewNote extends Named {

    private String content;





    private research19_Paragraph research19_paragraph;


    public research19_ReviewNote(
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

    public research19_Paragraph getResearch19_paragraph() {
        return research19_paragraph;
    }

    public void setResearch19_paragraph(research19_Paragraph research19_paragraph) {
        this.research19_paragraph = research19_paragraph;
    }

}