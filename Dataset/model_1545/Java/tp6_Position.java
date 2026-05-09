





import java.util.List;
import java.util.ArrayList;

public class tp6_Position  {

    private String description;
    private String name;





    private tp6_PublicationStructure tp6_publicationstructure;




    private tp6_Researcher tp6_researcher;




    private tp6_Position tp6_position;


    public tp6_Position(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
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
    public tp6_Researcher getTp6_researcher() {
        return tp6_researcher;
    }

    public void setTp6_researcher(tp6_Researcher tp6_researcher) {
        this.tp6_researcher = tp6_researcher;
    }
    public tp6_Position getTp6_position() {
        return tp6_position;
    }

    public void setTp6_position(tp6_Position tp6_position) {
        this.tp6_position = tp6_position;
    }

}