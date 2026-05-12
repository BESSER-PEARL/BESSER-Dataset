





import java.util.List;
import java.util.ArrayList;

public class Event1  {

    private boolean isOpen;
    private None location;
    private String name;
    private int size;
    private int rating;
    private String joined;
    private String date;
    private String invites;
    private None eventOwner;





    private List<Post1> post1s;




    private User1 user1;


    public Event1(
        boolean isOpen,        None location,        String name,        int size,        int rating,        String joined,        String date,        String invites,        None eventOwner    ) {
        this.isOpen = isOpen;
        this.location = location;
        this.name = name;
        this.size = size;
        this.rating = rating;
        this.joined = joined;
        this.date = date;
        this.invites = invites;
        this.eventOwner = eventOwner;
        this.post1s = new ArrayList<>();
    }

    public Event1(
        boolean isOpen,        None location,        String name,        int size,        int rating,        String joined,        String date,        String invites,        None eventOwner        ArrayList<Post1> post1s    ) {
        this.isOpen = isOpen;
        this.location = location;
        this.name = name;
        this.size = size;
        this.rating = rating;
        this.joined = joined;
        this.date = date;
        this.invites = invites;
        this.eventOwner = eventOwner;
        this.post1s = post1s;
    }

    public boolean getIsopen() {
        return isOpen;
    }

    public void setIsopen(boolean isOpen) {
        this.isOpen = isOpen;
    }
    public None getLocation() {
        return location;
    }

    public void setLocation(None location) {
        this.location = location;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public int getRating() {
        return rating;
    }

    public void setRating(int rating) {
        this.rating = rating;
    }
    public String getJoined() {
        return joined;
    }

    public void setJoined(String joined) {
        this.joined = joined;
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

    public List<Post1> getPost1s() {
        return post1s;
    }

    public void addPost1(Post1 post1) {
        this.post1s.add(post1);
    }
    public User1 getUser1() {
        return user1;
    }

    public void setUser1(User1 user1) {
        this.user1 = user1;
    }

}