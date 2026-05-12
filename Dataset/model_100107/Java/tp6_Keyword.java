





import java.util.List;
import java.util.ArrayList;

public class tp6_Keyword  {

    private String description;
    private String key;





    private tp6_PaperKeywords tp6_paperkeywords;




    private List<tp6_Paper> tp6_papers;




    private tp6_KnowledgeManager tp6_knowledgemanager;


    public tp6_Keyword(
        String description,        String key    ) {
        this.description = description;
        this.key = key;
        this.tp6_papers = new ArrayList<>();
    }

    public tp6_Keyword(
        String description,        String key        ArrayList<tp6_Paper> tp6_papers    ) {
        this.description = description;
        this.key = key;
        this.tp6_papers = tp6_papers;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }

    public tp6_PaperKeywords getTp6_paperkeywords() {
        return tp6_paperkeywords;
    }

    public void setTp6_paperkeywords(tp6_PaperKeywords tp6_paperkeywords) {
        this.tp6_paperkeywords = tp6_paperkeywords;
    }
    public List<tp6_Paper> getTp6_papers() {
        return tp6_papers;
    }

    public void addTp6_paper(Tp6_paper tp6_paper) {
        this.tp6_papers.add(tp6_paper);
    }
    public tp6_KnowledgeManager getTp6_knowledgemanager() {
        return tp6_knowledgemanager;
    }

    public void setTp6_knowledgemanager(tp6_KnowledgeManager tp6_knowledgemanager) {
        this.tp6_knowledgemanager = tp6_knowledgemanager;
    }

}