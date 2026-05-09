





import java.util.List;
import java.util.ArrayList;

public class publication2014b_Paper extends Named {






    private publication2014b_PublicationStructure publication2014b_publicationstructure;




    private List<publication2014b_Paragraph> publication2014b_paragraphs;


    public publication2014b_Paper(
    ) {
        super(
        );
        this.publication2014b_paragraphs = new ArrayList<>();
    }

    public publication2014b_Paper(
        ArrayList<publication2014b_Paragraph> publication2014b_paragraphs    ) {
        this.publication2014b_paragraphs = publication2014b_paragraphs;
    }


    public publication2014b_PublicationStructure getPublication2014b_publicationstructure() {
        return publication2014b_publicationstructure;
    }

    public void setPublication2014b_publicationstructure(publication2014b_PublicationStructure publication2014b_publicationstructure) {
        this.publication2014b_publicationstructure = publication2014b_publicationstructure;
    }
    public List<publication2014b_Paragraph> getPublication2014b_paragraphs() {
        return publication2014b_paragraphs;
    }

    public void addPublication2014b_paragraph(Publication2014b_paragraph publication2014b_paragraph) {
        this.publication2014b_paragraphs.add(publication2014b_paragraph);
    }

}