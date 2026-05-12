





import java.util.List;
import java.util.ArrayList;

public class Event1  {

    private String joined;
    private boolean isOpen;
    private int size;
    private String name;
    private String date;
    private String invites;
    private None eventOwner;
    private int rating;
    private None location;





    private User1 user1;




    private List<Post1> post1s;


    public Event1(
        String joined,        boolean isOpen,        int size,        String name,        String date,        String invites,        None eventOwner,        int rating,        None location    ) {
        this.joined = joined;
        this.isOpen = isOpen;
        this.size = size;
        this.name = name;
        this.date = date;
        this.invites = invites;
        this.eventOwner = eventOwner;
        this.rating = rating;
        this.location = location;
        this.post1s = new ArrayList<>();
    }

    public Event1(
        String joined,        boolean isOpen,        int size,        String name,        String date,        String invites,        None eventOwner,        int rating,        None location        ArrayList<Post1> post1s    ) {
        this.joined = joined;
        this.isOpen = isOpen;
        this.size = size;
        this.name = name;
        this.date = date;
        this.invites = invites;
        this.eventOwner = eventOwner;
        this.rating = rating;
        this.location = location;
        this.post1s = post1s;
    }

    public String getJoined() {
        return joined;
    }

    public void setJoined(String joined) {
        this.joined = joined;
    }
    public boolean getIsopen() {
        return isOpen;
    }

    public void setIsopen(boolean isOpen) {
        this.isOpen = isOpen;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getInvites() {
        return invites;
    }

    public void setInvites(String invites) {
        this.invites = invites;
    }
    public None getEventowner() {
        return eventOwner;
    }

    public void setEventowner(None eventOwner) {
        this.eventOwner = eventOwner;
    }
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }
    public None getLocation() {
        return location;
    }

    public void setLocation(None location) {
        this.location = location;
    }

    public User1 getUser1() {
        return user1;
    }

    public void setUser1(User1 user1) {
        this.user1 = user1;
    }
    public List<Post1> getPost1s() {
        return post1s;
    }

    public void addPost1(Post1 post1) {
        this.post1s.add(post1);
    }

}