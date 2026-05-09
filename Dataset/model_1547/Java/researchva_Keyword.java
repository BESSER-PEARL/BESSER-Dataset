





import java.util.List;
import java.util.ArrayList;

public class researchva_Keyword extends Named {

    private String word;





    private researchva_PublicationStructure researchva_publicationstructure;


    public researchva_Keyword(
        String word    ) {
        super(
        );
        this.word = word;
    }


    public String getWord() {
        return word;
    }

    public void setWord(String word) {
        this.word = word;
    }

    public researchva_PublicationStructure getResearchva_publicationstructure() {
        return researchva_publicationstructure;
    }

    public void setResearchva_publicationstructure(researchva_PublicationStructure researchva_publicationstructure) {
        this.researchva_publicationstructure = researchva_publicationstructure;
    }

}