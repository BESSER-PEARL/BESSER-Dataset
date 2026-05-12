





import java.util.List;
import java.util.ArrayList;

public class publication103_Position extends Named {

    private String description;





    private publication103_Researcher publication103_researcher;




    private publication103_Position publication103_position;




    private publication103_PublicationStructure publication103_publicationstructure;


    public publication103_Position(
        String description    ) {
        super(
        );
        this.description = description;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public publication103_Researcher getPublication103_researcher() {
        return publication103_researcher;
    }

    public void setPublication103_researcher(publication103_Researcher publication103_researcher) {
        this.publication103_researcher = publication103_researcher;
    }
    public publication103_Position getPublication103_position() {
        return publication103_position;
    }

    public void setPublication103_position(publication103_Position publication103_position) {
        this.publication103_position = publication103_position;
    }
    public publication103_PublicationStructure getPublication103_publicationstructure() {
        return publication103_publicationstructure;
    }

    public void setPublication103_publicationstructure(publication103_PublicationStructure publication103_publicationstructure) {
        this.publication103_publicationstructure = publication103_publicationstructure;
    }

}