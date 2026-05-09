





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Journal  {

    private String name;
    private String acronym;
    private boolean jcrIndexed;





    private sistedesMM_Article sistedesmm_article;




    private sistedesMM_Article sistedesmm_article;


    public sistedesMM_Journal(
        String name,        String acronym,        boolean jcrIndexed    ) {
        this.name = name;
        this.acronym = acronym;
        this.jcrIndexed = jcrIndexed;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAcronym() {
        return acronym;
    }

    public void setAcronym(String acronym) {
        this.acronym = acronym;
    }
    public boolean getJcrindexed() {
        return jcrIndexed;
    }

    public void setJcrindexed(boolean jcrIndexed) {
        this.jcrIndexed = jcrIndexed;
    }

    public sistedesMM_Article getSistedesmm_article() {
        return sistedesmm_article;
    }

    public void setSistedesmm_article(sistedesMM_Article sistedesmm_article) {
        this.sistedesmm_article = sistedesmm_article;
    }
    public sistedesMM_Article getSistedesmm_article() {
        return sistedesmm_article;
    }

    public void setSistedesmm_article(sistedesMM_Article sistedesmm_article) {
        this.sistedesmm_article = sistedesmm_article;
    }

}