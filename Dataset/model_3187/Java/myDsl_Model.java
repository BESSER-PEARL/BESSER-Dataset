





import java.util.List;
import java.util.ArrayList;

public class myDsl_Model  {






    private List<myDsl_Member> mydsl_members;


    public myDsl_Model(
    ) {
        this.mydsl_members = new ArrayList<>();
    }

    public myDsl_Model(
        ArrayList<myDsl_Member> mydsl_members    ) {
        this.mydsl_members = mydsl_members;
    }


    public List<myDsl_Member> getMydsl_members() {
        return mydsl_members;
    }

    public void addMydsl_member(Mydsl_member mydsl_member) {
        this.mydsl_members.add(mydsl_member);
    }

}