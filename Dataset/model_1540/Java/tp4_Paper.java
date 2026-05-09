





import java.util.List;
import java.util.ArrayList;

public class tp4_Paper extends Named {






    private List<tp4_Paragraph> tp4_paragraphs;




    private tp4_PublicationStructure tp4_publicationstructure;




    private List<tp4_Keyword> tp4_keywords;


    public tp4_Paper(
    ) {
        super(
        );
        this.tp4_paragraphs = new ArrayList<>();
        this.tp4_keywords = new ArrayList<>();
    }

    public tp4_Paper(
        ArrayList<tp4_Paragraph> tp4_paragraphs,        ArrayList<tp4_Keyword> tp4_keywords    ) {
        this.tp4_paragraphs = tp4_paragraphs;
        this.tp4_keywords = tp4_keywords;
    }


    public List<tp4_Paragraph> getTp4_paragraphs() {
        return tp4_paragraphs;
    }

    public void addTp4_paragraph(Tp4_paragraph tp4_paragraph) {
        this.tp4_paragraphs.add(tp4_paragraph);
    }
    public tp4_PublicationStructure getTp4_publicationstructure() {
        return tp4_publicationstructure;
    }

    public void setTp4_publicationstructure(tp4_PublicationStructure tp4_publicationstructure) {
        this.tp4_publicationstructure = tp4_publicationstructure;
    }
    public List<tp4_Keyword> getTp4_keywords() {
        return tp4_keywords;
    }

    public void addTp4_keyword(Tp4_keyword tp4_keyword) {
        this.tp4_keywords.add(tp4_keyword);
    }

}