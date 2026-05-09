





import java.util.List;
import java.util.ArrayList;

public class publication102_Paragraph extends Counted, Named {

    private String content;





    private publication102_Write publication102_write;




    private publication102_Paper publication102_paper;


    public publication102_Paragraph(
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

    public publication102_Write getPublication102_write() {
        return publication102_write;
    }

    public void setPublication102_write(publication102_Write publication102_write) {
        this.publication102_write = publication102_write;
    }
    public publication102_Paper getPublication102_paper() {
        return publication102_paper;
    }

    public void setPublication102_paper(publication102_Paper publication102_paper) {
        this.publication102_paper = publication102_paper;
    }

}