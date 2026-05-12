





import java.util.List;
import java.util.ArrayList;

public class tp6_Collaboration  {

    private int ratio;
    private String role;





    private tp6_Paper tp6_paper;




    private tp6_Researcher tp6_researcher;


    public tp6_Collaboration(
        int ratio,        String role    ) {
        this.ratio = ratio;
        this.role = role;
    }


    public int getRatio() {
        return ratio;
    }

    public void setRatio(int ratio) {
        this.ratio = ratio;
    }
    public String getRole() {
        return role;
    }

    public void setRole(String role) {
        this.role = role;
    }

    public tp6_Paper getTp6_paper() {
        return tp6_paper;
    }

    public void setTp6_paper(tp6_Paper tp6_paper) {
        this.tp6_paper = tp6_paper;
    }
    public tp6_Researcher getTp6_researcher() {
        return tp6_researcher;
    }

    public void setTp6_researcher(tp6_Researcher tp6_researcher) {
        this.tp6_researcher = tp6_researcher;
    }

}