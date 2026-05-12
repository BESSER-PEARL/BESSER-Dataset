





import java.util.List;
import java.util.ArrayList;

public class Ar_Condicionado  {

    private String borrowed_date;
    private String returned_date;
    private int member_id;
    private int fine_amount;
    private int book_id;





    private Members members;




    private List<Quado_Branco> quado_brancos;


    public Ar_Condicionado(
        String borrowed_date,        String returned_date,        int member_id,        int fine_amount,        int book_id    ) {
        this.borrowed_date = borrowed_date;
        this.returned_date = returned_date;
        this.member_id = member_id;
        this.fine_amount = fine_amount;
        this.book_id = book_id;
        this.quado_brancos = new ArrayList<>();
    }

    public Ar_Condicionado(
        String borrowed_date,        String returned_date,        int member_id,        int fine_amount,        int book_id        ArrayList<Quado_Branco> quado_brancos    ) {
        this.borrowed_date = borrowed_date;
        this.returned_date = returned_date;
        this.member_id = member_id;
        this.fine_amount = fine_amount;
        this.book_id = book_id;
        this.quado_brancos = quado_brancos;
    }

    public String getBorrowed_date() {
        return borrowed_date;
    }

    public void setBorrowed_date(String borrowed_date) {
        this.borrowed_date = borrowed_date;
    }
    public String getReturned_date() {
        return returned_date;
    }

    public void setReturned_date(String returned_date) {
        this.returned_date = returned_date;
    }
    public int getMember_id() {
        return member_id;
    }

    public void setMember_id(int member_id) {
        this.member_id = member_id;
    }
    public int getFine_amount() {
        return fine_amount;
    }

    public void setFine_amount(int fine_amount) {
        this.fine_amount = fine_amount;
    }
    public int getBook_id() {
        return book_id;
    }

    public void setBook_id(int book_id) {
        this.book_id = book_id;
    }

    public Members getMembers() {
        return members;
    }

    public void setMembers(Members members) {
        this.members = members;
    }
    public List<Quado_Branco> getQuado_brancos() {
        return quado_brancos;
    }

    public void addQuado_branco(Quado_branco quado_branco) {
        this.quado_brancos.add(quado_branco);
    }

}