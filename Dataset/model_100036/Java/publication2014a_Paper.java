





import java.util.List;
import java.util.ArrayList;

public class publication2014a_Paper extends Named {






    private publication2014a_PublicationStructure publication2014a_publicationstructure;




    private List<publication2014a_Paragraph> publication2014a_paragraphs;


    public publication2014a_Paper(
    ) {
        super(
        );
        this.publication2014a_paragraphs = new ArrayList<>();
    }

    public publication2014a_Paper(
        ArrayList<publication2014a_Paragraph> publication2014a_paragraphs    ) {
        this.publication2014a_paragraphs = publication2014a_paragraphs;
    }


    public publication2014a_PublicationStructure getPublication2014a_publicationstructure() {
        return publication2014a_publicationstructure;
    }

    public void setPublication2014a_publicationstructure(publication2014a_PublicationStructure publication2014a_publicationstructure) {
        this.publication2014a_publicationstructure = publication2014a_publicationstructure;
    }
    public List<publication2014a_Paragraph> getPublication2014a_paragraphs() {
        return publication2014a_paragraphs;
    }

    public void addPublication2014a_paragraph(Publication2014a_paragraph publication2014a_paragraph) {
        this.publication2014a_paragraphs.add(publication2014a_paragraph);
    }

}