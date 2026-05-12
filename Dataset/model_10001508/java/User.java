





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String tickets;
    private String id;
    private None birthdate;
    private String gender;
    private None events;
    private String password;
    private String friends;
    private String company;
    private String selfDescription;
    private String name;
    private String userImage;





    private List<Ticket> tickets;




    private List<Event> events;


    public User(
        String tickets,        String id,        None birthdate,        String gender,        None events,        String password,        String friends,        String company,        String selfDescription,        String name,        String userImage    ) {
        this.tickets = tickets;
        this.id = id;
        this.birthdate = birthdate;
        this.gender = gender;
        this.events = events;
        this.password = password;
        this.friends = friends;
        this.company = company;
        this.selfDescription = selfDescription;
        this.name = name;
        this.userImage = userImage;
        this.tickets = new ArrayList<>();
        this.events = new ArrayList<>();
    }

    public User(
        String tickets,        String id,        None birthdate,        String gender,        None events,        String password,        String friends,        String company,        String selfDescription,        String name,        String userImage        ArrayList<Ticket> tickets,        ArrayList<Event> events    ) {
        this.tickets = tickets;
        this.id = id;
        this.birthdate = birthdate;
        this.gender = gender;
        this.events = events;
        this.password = password;
        this.friends = friends;
        this.company = company;
        this.selfDescription = selfDescription;
        this.name = name;
        this.userImage = userImage;
        this.tickets = tickets;
        this.events = events;
    }

    public String getTickets() {
        return tickets;
    }

    public void setTickets(String tickets) {
        this.tickets = tickets;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public None getBirthdate() {
        return birthdate;
    }

    public void setBirthdate(None birthdate) {
        this.birthdate = birthdate;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public None getEvents() {
        return events;
    }

    public void setEvents(None events) {
        this.events = events;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public String getFriends() {
        return friends;
    }

    public void setFriends(String friends) {
        this.friends = friends;
    }
    public String getCompany() {
        return company;
    }

    public void setCompany(String company) {
        this.company = company;
    }
    public String getSelfdescription() {
        return selfDescription;
    }

    public void setSelfdescription(String selfDescription) {
        this.selfDescription = selfDescription;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUserimage() {
        return userImage;
    }

    public void setUserimage(String userImage) {
        this.userImage = userImage;
    }

    public List<Ticket> getTickets() {
        return tickets;
    }

    public void addTicket(Ticket ticket) {
        this.tickets.add(ticket);
    }
    public List<Event> getEvents() {
        return events;
    }

    public void addEvent(Event event) {
        this.events.add(event);
    }

}