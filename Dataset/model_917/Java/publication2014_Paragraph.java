





import java.util.List;
import java.util.ArrayList;

public class publication2014_Paragraph extends Counted, Named {

    private String content;





    private publication2014_Paper publication2014_paper;


    public publication2014_Paragraph(
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

    public publication2014_Paper getPublication2014_paper() {
        return publication2014_paper;
    }

    public void setPublication2014_paper(publication2014_Paper publication2014_paper) {
        this.publication2014_paper = publication2014_paper;
    }

}