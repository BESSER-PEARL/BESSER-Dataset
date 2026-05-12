





import java.util.List;
import java.util.ArrayList;

public class User  {

    private String name;





    private Registration registration;




    private List<Post> posts;




    private Profile profile;




    private List<Message> messages;




    private List<Page> pages;




    private Login login;




    private List<Group> groups;




    private List<Hashtag> hashtags;




    private List<Friend> friends;


    public User(
        String name    ) {
        this.name = name;
        this.posts = new ArrayList<>();
        this.messages = new ArrayList<>();
        this.pages = new ArrayList<>();
        this.groups = new ArrayList<>();
        this.hashtags = new ArrayList<>();
        this.friends = new ArrayList<>();
    }

    public User(
        String name        ArrayList<Post> posts,        ArrayList<Message> messages,        ArrayList<Page> pages,        ArrayList<Group> groups,        ArrayList<Hashtag> hashtags,        ArrayList<Friend> friends    ) {
        this.name = name;
        this.posts = posts;
        this.messages = messages;
        this.pages = pages;
        this.groups = groups;
        this.hashtags = hashtags;
        this.friends = friends;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Registration getRegistration() {
        return registration;
    }

    public void setRegistration(Registration registration) {
        this.registration = registration;
    }
    public List<Post> getPosts() {
        return posts;
    }

    public void addPost(Post post) {
        this.posts.add(post);
    }
    public Profile getProfile() {
        return profile;
    }

    public void setProfile(Profile profile) {
        this.profile = profile;
    }
    public List<Message> getMessages() {
        return messages;
    }

    public void addMessage(Message message) {
        this.messages.add(message);
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
    public List<Friend> getFriends() {
        return friends;
    }

    public void addFriend(Friend friend) {
        this.friends.add(friend);
    }

}