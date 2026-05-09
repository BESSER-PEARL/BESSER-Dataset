





import java.util.List;
import java.util.ArrayList;

public class Paper_Author  {

    private String name;
    private String email;





    private Paper_Paper paper_paper;


    public Paper_Author(
        String name,        String email    ) {
        this.name = name;
        this.email = email;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    public Paper_Paper getPaper_paper() {
        return paper_paper;
    }

    public void setPaper_paper(Paper_Paper paper_paper) {
        this.paper_paper = paper_paper;
    }

}