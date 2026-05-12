





import java.util.List;
import java.util.ArrayList;

public class Borrowed  {

    private String returned_date;
    private String borrowed_date;





    private List<Retro_Projetor> retro_projetors;




    private List<Members> memberss;


    public Borrowed(
        String returned_date,        String borrowed_date    ) {
        this.returned_date = returned_date;
        this.borrowed_date = borrowed_date;
        this.retro_projetors = new ArrayList<>();
        this.memberss = new ArrayList<>();
    }

    public Borrowed(
        String returned_date,        String borrowed_date        ArrayList<Retro_Projetor> retro_projetors,        ArrayList<Members> memberss    ) {
        this.returned_date = returned_date;
        this.borrowed_date = borrowed_date;
        this.retro_projetors = retro_projetors;
        this.memberss = memberss;
    }

    public String getReturned_date() {
        return returned_date;
    }

    public void setReturned_date(String returned_date) {
        this.returned_date = returned_date;
    }
    public String getBorrowed_date() {
        return borrowed_date;
    }

    public void setBorrowed_date(String borrowed_date) {
        this.borrowed_date = borrowed_date;
    }

    public List<Retro_Projetor> getRetro_projetors() {
        return retro_projetors;
    }

    public void addRetro_projetor(Retro_projetor retro_projetor) {
        this.retro_projetors.add(retro_projetor);
    }
    public List<Members> getMemberss() {
        return memberss;
    }

    public void addMembers(Members members) {
        this.memberss.add(members);
    }

}