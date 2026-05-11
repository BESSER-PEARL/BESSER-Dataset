





import java.util.List;
import java.util.ArrayList;

public class tdt4250_Course  {

    private int ID;
    private String name;
    private int credit;





    private List<tdt4250__bDYekCdxEeKsSJflfBDxuw> tdt4250__bdyekcdxeekssjflfbdxuws;


    public tdt4250_Course(
        int ID,        String name,        int credit    ) {
        this.ID = ID;
        this.name = name;
        this.credit = credit;
        this.tdt4250__bdyekcdxeekssjflfbdxuws = new ArrayList<>();
    }

    public tdt4250_Course(
        int ID,        String name,        int credit        ArrayList<tdt4250__bDYekCdxEeKsSJflfBDxuw> tdt4250__bdyekcdxeekssjflfbdxuws    ) {
        this.ID = ID;
        this.name = name;
        this.credit = credit;
        this.tdt4250__bdyekcdxeekssjflfbdxuws = tdt4250__bdyekcdxeekssjflfbdxuws;
    }

    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getCredit() {
        return credit;
    }

    public void setCredit(int credit) {
        this.credit = credit;
    }

    public List<tdt4250__bDYekCdxEeKsSJflfBDxuw> getTdt4250__bdyekcdxeekssjflfbdxuws() {
        return tdt4250__bdyekcdxeekssjflfbdxuws;
    }

    public void addTdt4250__bdyekcdxeekssjflfbdxuw(Tdt4250__bdyekcdxeekssjflfbdxuw tdt4250__bdyekcdxeekssjflfbdxuw) {
        this.tdt4250__bdyekcdxeekssjflfbdxuws.add(tdt4250__bdyekcdxeekssjflfbdxuw);
    }

}