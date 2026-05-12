





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String name;





    private List<Friend> friends;




    private List<Message> messages;




    private Login login;




    private Registration registration;




    private List<Group> groups;




    private List<Hashtag> hashtags;




    private List<Page> pages;


    public User(
        String name    ) {
        this.name = name;
        this.friends = new ArrayList<>();
        this.messages = new ArrayList<>();
        this.groups = new ArrayList<>();
        this.hashtags = new ArrayList<>();
        this.pages = new ArrayList<>();
    }

    public User(
        String name        ArrayList<Friend> friends,        ArrayList<Message> messages,        ArrayList<Group> groups,        ArrayList<Hashtag> hashtags,        ArrayList<Page> pages    ) {
        this.name = name;
        this.friends = friends;
        this.messages = messages;
        this.groups = groups;
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
    public List<Message> getMessages() {
        return messages;
    }

    public void addMessage(Message message) {
        this.messages.add(message);
    }
    public Login getLogin() {
        return login;
    }

    public void setLogin(Login login) {
        this.login = login;
    }
    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }
    public List<Group> getGroups() {
        return groups;
    }

    public void addGroup(Group group) {
        this.groups.add(group);
    }
    public List<Hashtag> getHashtags() {
        return hashtags;
    }

    public void addHashtag(Hashtag hashtag) {
        this.hashtags.add(hashtag);
    }
    public List<Page> getPages() {
        return pages;
    }

    public void addPage(Page page) {
        this.pages.add(page);
    }

}