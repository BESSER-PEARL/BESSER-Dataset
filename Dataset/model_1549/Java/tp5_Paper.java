





import java.util.List;
import java.util.ArrayList;

public class tp5_Paper  {

    private String name;





    private List<tp5_Researcher> tp5_researchers;




    private tp5_Paper tp5_paper;




    private tp5_Researcher tp5_researcher;


    public tp5_Paper(
        String name    ) {
        this.name = name;
        this.tp5_researchers = new ArrayList<>();
    }

    public tp5_Paper(
        String name        ArrayList<tp5_Researcher> tp5_researchers    ) {
        this.name = name;
        this.tp5_researchers = tp5_researchers;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<tp5_Researcher> getTp5_researchers() {
        return tp5_researchers;
    }

    public void addTp5_researcher(Tp5_researcher tp5_researcher) {
        this.tp5_researchers.add(tp5_researcher);
    }
    public tp5_Paper getTp5_paper() {
        return tp5_paper;
    }

    public void setTp5_paper(tp5_Paper tp5_paper) {
        this.tp5_paper = tp5_paper;
    }
    public tp5_Researcher getTp5_researcher() {
        return tp5_researcher;
    }

    public void setTp5_researcher(tp5_Researcher tp5_researcher) {
        this.tp5_researcher = tp5_researcher;
    }

}