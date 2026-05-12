





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_Journal  {

    private boolean jcrIndexed;
    private String acronym;
    private String name;





    private sistedesMM_Article sistedesmm_article;




    private sistedesMM_Article sistedesmm_article;


    public sistedesMM_Journal(
        boolean jcrIndexed,        String acronym,        String name    ) {
        this.jcrIndexed = jcrIndexed;
        this.acronym = acronym;
        this.name = name;
    }


    public boolean getJcrindexed() {
        return jcrIndexed;
    }

    public void setJcrindexed(boolean jcrIndexed) {
        this.jcrIndexed = jcrIndexed;
    }
    public String getAcronym() {
        return acronym;
    }

    public void setAcronym(String acronym) {
        this.acronym = acronym;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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