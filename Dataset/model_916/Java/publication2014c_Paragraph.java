





import java.util.List;
import java.util.ArrayList;

public class publication2014c_Paragraph extends Named, Counted {

    private String content;





    private publication2014c_Paper publication2014c_paper;


    public publication2014c_Paragraph(
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

    public publication2014c_Paper getPublication2014c_paper() {
        return publication2014c_paper;
    }

    public void setPublication2014c_paper(publication2014c_Paper publication2014c_paper) {
        this.publication2014c_paper = publication2014c_paper;
    }

}