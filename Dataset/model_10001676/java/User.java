





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String name;





    private List<Friend> friends;




    private List<Hashtag> hashtags;




    private Sign_Up sign_up;




    private List<Page> pages;




    private Login login;


    public User(
        String name    ) {
        this.name = name;
        this.friends = new ArrayList<>();
        this.hashtags = new ArrayList<>();
        this.pages = new ArrayList<>();
    }

    public User(
        String name        ArrayList<Friend> friends,        ArrayList<Hashtag> hashtags,        ArrayList<Page> pages    ) {
        this.name = name;
        this.friends = friends;
        this.hashtags = hashtags;
        this.pages = pages;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<Friend> getFriends() {
        return friends;
    }

    public void addFriend(Friend friend) {
        this.friends.add(friend);
    }
    public List<Hashtag> getHashtags() {
        return hashtags;
    }

    public void addHashtag(Hashtag hashtag) {
        this.hashtags.add(hashtag);
    }
    public Sign_Up getSign_up() {
        return sign_up;
    }

    public void setSign_up(Sign_Up sign_up) {
        this.sign_up = sign_up;
    }
    public List<Page> getPages() {
        return pages;
    }

    public void addPage(Page page) {
        this.pages.add(page);
    }
    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }

}