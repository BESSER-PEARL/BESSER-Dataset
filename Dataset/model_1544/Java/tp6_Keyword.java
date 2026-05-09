





import java.util.List;
import java.util.ArrayList;

public class tp6_Keyword  {

    private String key;
    private String description;





    private List<tp6_Paper> tp6_papers;


    public tp6_Keyword(
        String key,        String description    ) {
        this.key = key;
        this.description = description;
        this.tp6_papers = new ArrayList<>();
    }

    public tp6_Keyword(
        String key,        String description        ArrayList<tp6_Paper> tp6_papers    ) {
        this.key = key;
        this.description = description;
        this.tp6_papers = tp6_papers;
    }

    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public List<tp6_Paper> getTp6_papers() {
        return tp6_papers;
    }

    public void addTp6_paper(Tp6_paper tp6_paper) {
        this.tp6_papers.add(tp6_paper);
    }

}