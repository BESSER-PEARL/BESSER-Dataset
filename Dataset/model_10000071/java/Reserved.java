





import java.util.List;
import java.util.ArrayList;

public class Reserved  {

    private String reserved_date;





    private List<Members> memberss;




    private List<Retro_Projetor> retro_projetors;


    public Reserved(
        String reserved_date    ) {
        this.reserved_date = reserved_date;
        this.memberss = new ArrayList<>();
        this.retro_projetors = new ArrayList<>();
    }

    public Reserved(
        String reserved_date        ArrayList<Members> memberss,        ArrayList<Retro_Projetor> retro_projetors    ) {
        this.reserved_date = reserved_date;
        this.memberss = memberss;
        this.retro_projetors = retro_projetors;
    }

    public String getReserved_date() {
        return reserved_date;
    }

    public void setReserved_date(String reserved_date) {
        this.reserved_date = reserved_date;
    }

    public List<Members> getMemberss() {
        return memberss;
    }

    public void addMembers(Members members) {
        this.memberss.add(members);
    }
    public List<Retro_Projetor> getRetro_projetors() {
        return retro_projetors;
    }

    public void addRetro_projetor(Retro_projetor retro_projetor) {
        this.retro_projetors.add(retro_projetor);
    }

}