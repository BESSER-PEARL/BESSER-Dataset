





import java.util.List;
import java.util.ArrayList;

public class tp6_KnowledgeManager  {

    private String name;





    private tp6_PublicationStructure tp6_publicationstructure;


    public tp6_KnowledgeManager(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public tp6_PublicationStructure getTp6_publicationstructure() {
        return tp6_publicationstructure;
    }

    public void setTp6_publicationstructure(tp6_PublicationStructure tp6_publicationstructure) {
        this.tp6_publicationstructure = tp6_publicationstructure;
    }

}