





import java.util.List;
import java.util.ArrayList;

public class e_ticket  {

    private String status;
    private int id_user;
    private int id_ticket;
    private String due_date;
    private int id_event;
    private String date;
    private String bukti_trf;





    private List<user> users;


    public e_ticket(
        String status,        int id_user,        int id_ticket,        String due_date,        int id_event,        String date,        String bukti_trf    ) {
        this.status = status;
        this.id_user = id_user;
        this.id_ticket = id_ticket;
        this.due_date = due_date;
        this.id_event = id_event;
        this.date = date;
        this.bukti_trf = bukti_trf;
        this.users = new ArrayList<>();
    }

    public e_ticket(
        String status,        int id_user,        int id_ticket,        String due_date,        int id_event,        String date,        String bukti_trf        ArrayList<user> users    ) {
        this.status = status;
        this.id_user = id_user;
        this.id_ticket = id_ticket;
        this.due_date = due_date;
        this.id_event = id_event;
        this.date = date;
        this.bukti_trf = bukti_trf;
        this.users = users;
    }

    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public int getId_user() {
        return id_user;
    }

    public void setId_user(int id_user) {
        this.id_user = id_user;
    }
    public int getId_ticket() {
        return id_ticket;
    }

    public void setId_ticket(int id_ticket) {
        this.id_ticket = id_ticket;
    }
    public String getDue_date() {
        return due_date;
    }

    public void setDue_date(String due_date) {
        this.due_date = due_date;
    }
    public int getId_event() {
        return id_event;
    }

    public void setId_event(int id_event) {
        this.id_event = id_event;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getBukti_trf() {
        return bukti_trf;
    }

    public void setBukti_trf(String bukti_trf) {
        this.bukti_trf = bukti_trf;
    }

    public List<user> getUsers() {
        return users;
    }

    public void addUser(User user) {
        this.users.add(user);
    }

}