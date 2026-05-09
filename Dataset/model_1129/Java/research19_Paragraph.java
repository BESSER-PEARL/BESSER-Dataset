





import java.util.List;
import java.util.ArrayList;

public class research19_Paragraph extends Named, Counted {

    private String content;





    private research19_Paper research19_paper;




    private research19_Write research19_write;


    public research19_Paragraph(
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

    public research19_Paper getResearch19_paper() {
        return research19_paper;
    }

    public void setResearch19_paper(research19_Paper research19_paper) {
        this.research19_paper = research19_paper;
    }
    public research19_Write getResearch19_write() {
        return research19_write;
    }

    public void setResearch19_write(research19_Write research19_write) {
        this.research19_write = research19_write;
    }

}