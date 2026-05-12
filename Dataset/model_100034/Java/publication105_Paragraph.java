





import java.util.List;
import java.util.ArrayList;

public class publication105_Paragraph extends Counted, Named {

    private String content;





    private publication105_Write publication105_write;




    private publication105_Paper publication105_paper;


    public publication105_Paragraph(
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

    public publication105_Write getPublication105_write() {
        return publication105_write;
    }

    public void setPublication105_write(publication105_Write publication105_write) {
        this.publication105_write = publication105_write;
    }
    public publication105_Paper getPublication105_paper() {
        return publication105_paper;
    }

    public void setPublication105_paper(publication105_Paper publication105_paper) {
        this.publication105_paper = publication105_paper;
    }

}