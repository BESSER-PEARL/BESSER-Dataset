





import java.util.List;
import java.util.ArrayList;

public class tp4_Keyword extends Named {

    private String description;





    private tp4_Paper tp4_paper;


    public tp4_Keyword(
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

    public tp4_Paper getTp4_paper() {
        return tp4_paper;
    }

    public void setTp4_paper(tp4_Paper tp4_paper) {
        this.tp4_paper = tp4_paper;
    }

}