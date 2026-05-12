





import java.util.List;
import java.util.ArrayList;

public class research_Researcher  {

    private String name;
    private String forName;





    private research_PublicationStructure research_publicationstructure;


    public research_Researcher(
        String name,        String forName    ) {
        this.name = name;
        this.forName = forName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getForname() {
        return forName;
    }

    public void setForname(String forName) {
        this.forName = forName;
    }

    public research_PublicationStructure getResearch_publicationstructure() {
        return research_publicationstructure;
    }

    public void setResearch_publicationstructure(research_PublicationStructure research_publicationstructure) {
        this.research_publicationstructure = research_publicationstructure;
    }

}