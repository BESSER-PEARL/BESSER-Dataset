





import java.util.List;
import java.util.ArrayList;

public class publication101_Paper extends Named {






    private publication101_Paper publication101_paper;




    private List<publication101_Paragraph> publication101_paragraphs;




    private publication101_PublicationStructure publication101_publicationstructure;




    private publication101_Keyword publication101_keyword;


    public publication101_Paper(
    ) {
        super(
        );
        this.publication101_paragraphs = new ArrayList<>();
    }

    public publication101_Paper(
        ArrayList<publication101_Paragraph> publication101_paragraphs    ) {
        this.publication101_paragraphs = publication101_paragraphs;
    }


    public publication101_Paper getPublication101_paper() {
        return publication101_paper;
    }

    public void setPublication101_paper(publication101_Paper publication101_paper) {
        this.publication101_paper = publication101_paper;
    }
    public List<publication101_Paragraph> getPublication101_paragraphs() {
        return publication101_paragraphs;
    }

    public void addPublication101_paragraph(Publication101_paragraph publication101_paragraph) {
        this.publication101_paragraphs.add(publication101_paragraph);
    }
    public publication101_PublicationStructure getPublication101_publicationstructure() {
        return publication101_publicationstructure;
    }

    public void setPublication101_publicationstructure(publication101_PublicationStructure publication101_publicationstructure) {
        this.publication101_publicationstructure = publication101_publicationstructure;
    }
    public publication101_Keyword getPublication101_keyword() {
        return publication101_keyword;
    }

    public void setPublication101_keyword(publication101_Keyword publication101_keyword) {
        this.publication101_keyword = publication101_keyword;
    }

}