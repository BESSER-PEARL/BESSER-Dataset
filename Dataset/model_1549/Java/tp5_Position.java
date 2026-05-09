





import java.util.List;
import java.util.ArrayList;

public class tp5_Position  {

    private String name;
    private String description;





    private tp5_Position tp5_position;




    private tp5_Researcher tp5_researcher;




    private tp5_PublicationStructure tp5_publicationstructure;


    public tp5_Position(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public tp5_Position getTp5_position() {
        return tp5_position;
    }

    public void setTp5_position(tp5_Position tp5_position) {
        this.tp5_position = tp5_position;
    }
    public tp5_Researcher getTp5_researcher() {
        return tp5_researcher;
    }

    public void setTp5_researcher(tp5_Researcher tp5_researcher) {
        this.tp5_researcher = tp5_researcher;
    }
    public tp5_PublicationStructure getTp5_publicationstructure() {
        return tp5_publicationstructure;
    }

    public void setTp5_publicationstructure(tp5_PublicationStructure tp5_publicationstructure) {
        this.tp5_publicationstructure = tp5_publicationstructure;
    }

}