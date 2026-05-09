





import java.util.List;
import java.util.ArrayList;

public class publication_Paragraph extends Named, Counted {

    private String content;





    private publication_Paper publication_paper;


    public publication_Paragraph(
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

    public publication_Paper getPublication_paper() {
        return publication_paper;
    }

    public void setPublication_paper(publication_Paper publication_paper) {
        this.publication_paper = publication_paper;
    }

}