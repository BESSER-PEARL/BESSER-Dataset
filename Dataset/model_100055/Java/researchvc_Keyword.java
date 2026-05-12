





import java.util.List;
import java.util.ArrayList;

public class researchvc_Keyword extends Named {

    private String word;





    private researchvc_PublicationStructure researchvc_publicationstructure;




    private researchvc_PaperKeyword researchvc_paperkeyword;


    public researchvc_Keyword(
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

    public researchvc_PublicationStructure getResearchvc_publicationstructure() {
        return researchvc_publicationstructure;
    }

    public void setResearchvc_publicationstructure(researchvc_PublicationStructure researchvc_publicationstructure) {
        this.researchvc_publicationstructure = researchvc_publicationstructure;
    }
    public researchvc_PaperKeyword getResearchvc_paperkeyword() {
        return researchvc_paperkeyword;
    }

    public void setResearchvc_paperkeyword(researchvc_PaperKeyword researchvc_paperkeyword) {
        this.researchvc_paperkeyword = researchvc_paperkeyword;
    }

}